
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375), (63, 4.875, 0.375), (60, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.875, 0.1875), (67, 1.875, 0.1875), (70, 1.875, 0.1875),  # Dm7 on 2
    (62, 2.625, 0.1875), (67, 2.625, 0.1875), (70, 2.625, 0.1875),  # Dm7 on 4
    # Bar 3 (3.0 - 4.5s)
    (62, 3.875, 0.1875), (67, 3.875, 0.1875), (70, 3.875, 0.1875),  # Dm7 on 2
    (62, 4.625, 0.1875), (67, 4.625, 0.1875), (70, 4.625, 0.1875),  # Dm7 on 4
    # Bar 4 (4.5 - 6.0s)
    (62, 5.875, 0.1875), (67, 5.875, 0.1875), (70, 5.875, 0.1875)   # Dm7 on 2
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax (Dante): Melody - one short motif, sing it, leave it hanging, finish it
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375),  # motif
    # Bar 3 (3.0 - 4.5s)
    (65, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375),  # resolve
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375), (65, 4.875, 0.375), (67, 5.25, 0.375),  # restate
    (64, 5.625, 0.375)  # leave it hanging slightly
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue for full 6 seconds
drum_notes = []
for bar in range(2, 5):
    for beat in range(4):
        start = 1.5 + (bar - 2) * 1.5 + beat * 0.75
        drum_notes.append((36, start, 0.375))
        drum_notes.append((38, start + 0.375, 0.375))
        drum_notes.append((42, start, 0.1875))
        drum_notes.append((42, start + 0.375, 0.1875))
        drum_notes.append((42, start + 0.75, 0.1875))
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
