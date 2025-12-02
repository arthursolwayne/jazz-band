
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (40, 1.5, 0.375), (39, 1.875, 0.375), (41, 2.25, 0.375), (40, 2.625, 0.375),
    (38, 2.875, 0.375), (39, 3.25, 0.375), (41, 3.625, 0.375), (40, 4.0, 0.375),
    (38, 4.375, 0.375), (39, 4.75, 0.375), (41, 5.125, 0.375), (40, 5.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4, Fm7, Bb7, Eb7, Ab7
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (59, 1.5, 0.375), (60, 1.5, 0.375), (62, 1.5, 0.375), (63, 1.5, 0.375),
    (59, 2.25, 0.375), (60, 2.25, 0.375), (62, 2.25, 0.375), (63, 2.25, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (56, 3.0, 0.375), (57, 3.0, 0.375), (59, 3.0, 0.375), (60, 3.0, 0.375),
    (56, 3.75, 0.375), (57, 3.75, 0.375), (59, 3.75, 0.375), (60, 3.75, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (53, 4.5, 0.375), (54, 4.5, 0.375), (56, 4.5, 0.375), (57, 4.5, 0.375),
    (53, 5.25, 0.375), (54, 5.25, 0.375), (56, 5.25, 0.375), (57, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5, 0.375), (42, 1.5, 0.125),
    (38, 1.875, 0.375), (42, 1.875, 0.125),
    (36, 2.25, 0.375), (42, 2.25, 0.125),
    (38, 2.625, 0.375), (42, 2.625, 0.125),
    # Bar 3 (3.0 - 4.5s)
    (36, 3.0, 0.375), (42, 3.0, 0.125),
    (38, 3.375, 0.375), (42, 3.375, 0.125),
    (36, 3.75, 0.375), (42, 3.75, 0.125),
    (38, 4.125, 0.375), (42, 4.125, 0.125),
    # Bar 4 (4.5 - 6.0s)
    (36, 4.5, 0.375), (42, 4.5, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125),
    (36, 5.25, 0.375), (42, 5.25, 0.125),
    (38, 5.625, 0.375), (42, 5.625, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax motif
# Start with a simple motif on Fm, leave it hanging
sax_notes = [
    (62, 1.5, 0.375),  # F
    (60, 1.875, 0.375),  # Eb
    (58, 2.25, 0.375),  # D
    (62, 2.625, 0.375),  # F
    (62, 2.875, 0.375),  # F (hold)
    (62, 3.0, 0.375),  # F (hold)
    (62, 3.25, 0.375),  # F (hold)
    (62, 3.5, 0.375),  # F (hold)
    (62, 3.75, 0.375),  # F (hold)
    (62, 4.0, 0.375),  # F (hold)
    (62, 4.25, 0.375),  # F (hold)
    (62, 4.5, 0.375),  # F (hold)
    (62, 4.75, 0.375),  # F (hold)
    (62, 5.0, 0.375),  # F (hold)
    (62, 5.25, 0.375),  # F (hold)
    (62, 5.5, 0.375),  # F (hold)
    (62, 5.75, 0.375),  # F (hold)
    (62, 6.0, 0.375)  # F (hold)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("fmintrous.mid")
