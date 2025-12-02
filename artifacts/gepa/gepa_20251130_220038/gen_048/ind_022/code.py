
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat on 1
    (38, 0.375, 0.125), # Snare on 2
    (42, 0.375, 0.125), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.125),  # Hihat on 3
    (38, 1.125, 0.125), # Snare on 4
    (42, 1.125, 0.125), # Hihat on 4
    (42, 1.375, 0.125)  # Hihat on 4 (end)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),   # D4
    (63, 1.875, 0.375), # Eb4
    (64, 2.25, 0.375),  # E4
    (65, 2.625, 0.375), # F4
    (67, 2.999, 0.375), # G4
    (69, 3.375, 0.375), # A4
    (71, 3.75, 0.375),  # B4
    (72, 4.125, 0.375), # C5
    (71, 4.5, 0.375),   # B4
    (70, 4.875, 0.375), # Bb4
    (68, 5.25, 0.375),  # A4
    (67, 5.625, 0.375)  # G4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
# Comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.875, 0.25), # G4 (7th chord on 2)
    (72, 1.875, 0.25), # C5
    (74, 1.875, 0.25), # D5
    (69, 1.875, 0.25), # A4
    # Bar 3
    (72, 3.375, 0.25), # C5 (7th chord on 2)
    (74, 3.375, 0.25), # D5
    (76, 3.375, 0.25), # E5
    (71, 3.375, 0.25), # B4
    # Bar 4
    (67, 4.875, 0.25), # G4 (7th chord on 2)
    (72, 4.875, 0.25), # C5
    (74, 4.875, 0.25), # D5
    (69, 4.875, 0.25), # A4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante: Melody - short motif, make it sing
# D, F#, A (Dorian), then leave it hanging
sax_notes = [
    (62, 1.5, 0.5),    # D4
    (66, 2.0, 0.5),    # F#4
    (67, 2.5, 0.5),    # G4
    (62, 3.0, 0.5),    # D4
    (66, 3.5, 0.5),    # F#4
    (67, 4.0, 0.5),    # G4
    (69, 4.5, 0.5),    # A4
    (67, 5.0, 0.5),    # G4
    (66, 5.5, 0.5),    # F#4
    (64, 6.0, 0.5)     # E4 (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start, 0.375),  # Kick on 1
        (42, start, 0.125),  # Hihat on 1
        (38, start + 0.375, 0.125), # Snare on 2
        (42, start + 0.375, 0.125), # Hihat on 2
        (36, start + 0.75, 0.375),  # Kick on 3
        (42, start + 0.75, 0.125),  # Hihat on 3
        (38, start + 1.125, 0.125), # Snare on 4
        (42, start + 1.125, 0.125), # Hihat on 4
        (42, start + 1.375, 0.125)  # Hihat on 4 (end)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
