
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.375),
    (36, 1.125, 0.375), (38, 1.5, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D
bass_notes = [
    (65, 1.5, 0.375), (67, 1.875, 0.375), (69, 2.25, 0.375), (64, 2.625, 0.375),
    (66, 2.95, 0.375), (68, 3.325, 0.375), (70, 3.7, 0.375), (65, 4.075, 0.375),
    (67, 4.45, 0.375), (69, 4.825, 0.375), (64, 5.2, 0.375), (66, 5.575, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4, in D
piano_notes = [
    # Bar 2: D7 on beat 2
    (62, 2.25, 0.375), (67, 2.25, 0.375), (64, 2.25, 0.375), (69, 2.25, 0.375),
    # Bar 3: D7 on beat 2
    (62, 3.7, 0.375), (67, 3.7, 0.375), (64, 3.7, 0.375), (69, 3.7, 0.375),
    # Bar 4: D7 on beat 2
    (62, 5.2, 0.375), (67, 5.2, 0.375), (64, 5.2, 0.375), (69, 5.2, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start, 0.375), (38, start + 0.375, 0.375), (42, start + 0.75, 0.375),
        (36, start + 1.125, 0.375), (38, start + 1.5, 0.375)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Dante: Melody in D, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start of motif
sax_notes = [
    (62, 1.5, 0.75),  # D4
    (66, 2.25, 0.375),  # F#4
    (67, 2.625, 0.375),  # G4
    (69, 3.0, 0.375),  # A4
    (67, 3.375, 0.375),  # G4
    (66, 3.75, 0.375),  # F#4
    (64, 4.125, 0.375),  # E4
    (62, 4.5, 0.375),  # D4
    (64, 4.875, 0.375),  # E4
    (66, 5.25, 0.375),  # F#4
    (69, 5.625, 0.375),  # A4
    (67, 6.0, 0.375)  # G4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
