
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    (0.0, 36, 100), (0.75, 36, 100),
    # Snare on 2 and 4
    (0.375, 38, 100), (1.125, 38, 100),
    # Hihat on every eighth
    (0.0, 42, 100), (0.375, 42, 100), (0.75, 42, 100), (1.125, 42, 100)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 59, 100), (1.875, 60, 100), (2.25, 58, 100), (2.625, 57, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 59, 100), (3.375, 60, 100), (3.75, 58, 100), (4.125, 57, 100),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 59, 100), (4.875, 60, 100), (5.25, 58, 100), (5.625, 57, 100)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 62, 100), (1.75, 67, 100), (2.25, 62, 100), (2.25, 67, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.25, 62, 100), (3.25, 67, 100), (3.75, 62, 100), (3.75, 67, 100),
    # Bar 4 (4.5 - 6.0s)
    (4.75, 62, 100), (4.75, 67, 100), (5.25, 62, 100), (5.25, 67, 100)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.375)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.375)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.375)
    # Add to drum instrument
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 chord: D F A C
# Motif: D (1/2 beat), F (1/2 beat), A (1/2 beat), C (1/2 beat) -> repeat but shift up a half step
sax_notes = [
    (1.5, 62, 100), (1.75, 65, 100), (2.0, 67, 100), (2.25, 71, 100),
    (2.625, 64, 100), (2.875, 67, 100), (3.125, 69, 100), (3.375, 73, 100),
    (3.75, 62, 100), (4.0, 65, 100), (4.25, 67, 100), (4.5, 71, 100),
    (4.875, 64, 100), (5.125, 67, 100), (5.375, 69, 100), (5.625, 73, 100)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
