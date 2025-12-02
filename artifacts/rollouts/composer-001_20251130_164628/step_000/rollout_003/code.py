
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 57, 100), # D
    (1.875, 58, 100), # Eb
    (2.25, 59, 100), # E
    (2.625, 60, 100), # F
    # Bar 3
    (3.0, 62, 100), # G
    (3.375, 61, 100), # F#
    (3.75, 60, 100), # F
    (4.125, 59, 100), # E
    # Bar 4
    (4.5, 58, 100), # Eb
    (4.875, 57, 100), # D
    (5.25, 56, 100), # C
    (5.625, 60, 100), # F
]
for note in bass_notes:
    start, pitch, velocity = note
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 62, 100), # G7 (G B D F)
    (1.875, 67, 100), # B
    (1.875, 69, 100), # D
    (1.875, 64, 100), # F
    # Bar 3
    (3.375, 60, 100), # F7 (F A C Eb)
    (3.375, 65, 100), # A
    (3.375, 67, 100), # C
    (3.375, 64, 100), # Eb
    # Bar 4
    (4.875, 62, 100), # G7 (G B D F)
    (4.875, 67, 100), # B
    (4.875, 69, 100), # D
    (4.875, 64, 100), # F
]
for note in piano_notes:
    start, pitch, velocity = note
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

# Sax: Melody with a short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (1.5, 62, 100), # G
    (1.75, 65, 100), # Bb
    (2.0, 64, 100), # A
    # Bar 3
    (3.0, 62, 100), # G
    (3.25, 65, 100), # Bb
    (3.5, 64, 100), # A
    # Bar 4
    (4.5, 62, 100), # G
    (4.75, 65, 100), # Bb
    (5.0, 64, 100), # A
]
for note in sax_notes:
    start, pitch, velocity = note
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
