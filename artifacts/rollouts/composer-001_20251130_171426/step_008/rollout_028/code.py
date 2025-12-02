
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D (root)
    (63, 1.875, 0.375), # Eb (chromatic)
    (60, 2.25, 0.375),  # Bb (3rd)
    (62, 2.625, 0.375), # D (root)
    (63, 2.625, 0.375), # Eb (chromatic)
    (60, 3.0, 0.375),   # Bb (3rd)
    (62, 3.375, 0.375), # D (root)
    (63, 3.75, 0.375),  # Eb (chromatic)
    (60, 4.125, 0.375), # Bb (3rd)
    (62, 4.5, 0.375),   # D (root)
    (63, 4.875, 0.375), # Eb (chromatic)
    (60, 5.25, 0.375)   # Bb (3rd)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.1875),  # D7 (D, F#, C, Bb)
    (67, 1.5, 0.1875),
    (69, 1.5, 0.1875),
    (64, 1.5, 0.1875),
    (62, 2.25, 0.1875), # D7
    (67, 2.25, 0.1875),
    (69, 2.25, 0.1875),
    (64, 2.25, 0.1875),
    # Bar 3
    (62, 3.0, 0.1875),  # D7
    (67, 3.0, 0.1875),
    (69, 3.0, 0.1875),
    (64, 3.0, 0.1875),
    (62, 3.75, 0.1875), # D7
    (67, 3.75, 0.1875),
    (69, 3.75, 0.1875),
    (64, 3.75, 0.1875),
    # Bar 4
    (62, 4.5, 0.1875),  # D7
    (67, 4.5, 0.1875),
    (69, 4.5, 0.1875),
    (64, 4.5, 0.1875),
    (62, 5.25, 0.1875), # D7
    (67, 5.25, 0.1875),
    (69, 5.25, 0.1875),
    (64, 5.25, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Bar 2: start=3.0, end=4.5
    # Bar 3: start=4.5, end=6.0
    # Bar 4: start=6.0, end=7.5 (but we only go to 6.0)
    for beat in range(0, 4):
        time = start + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1875))

# Saxophone (Dante): short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.1875),  # D (root)
    (66, 1.6875, 0.1875), # F# (3rd)
    (62, 2.0, 0.1875),  # D (root)
    (72, 2.1875, 0.1875), # Bb (7th)
    (62, 4.5, 0.1875),  # D (root)
    (66, 4.6875, 0.1875), # F# (3rd)
    (62, 5.0, 0.1875),  # D (root)
    (72, 5.1875, 0.1875)  # Bb (7th)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
