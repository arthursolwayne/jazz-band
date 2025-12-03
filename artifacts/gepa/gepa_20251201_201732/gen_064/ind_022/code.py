
import pretty_midi

# Initialize MIDI with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Define the time for each bar (160 BPM, 4/4 time)
bar_duration = 1.5  # in seconds

# Bar 1: Little Ray alone (drums only)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Time: 0.0 to 1.5s
drum_notes = [
    # Bar 1
    (0.0, drum_kick), (0.375, drum_hihat), (0.75, drum_kick), (0.75, drum_snare),
    (1.125, drum_hihat), (1.5, drum_kick), (1.5, drum_snare)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 to 3.0s)
# 1.5 to 3.0s

# Bass: Walking line in F minor, roots and fifths with chromatic approaches
# Bar 2: F - E - D - C
# Bar 3: F - G - A - Bb
# Bar 4: F - E - Bb - C

# Bass notes (start time, pitch)
bass_notes = [
    (1.5, 71), (1.875, 70), (2.25, 69), (2.625, 67),
    (3.0, 71), (3.375, 72), (3.75, 74), (4.125, 71),
    (4.5, 71), (4.875, 70), (5.25, 76), (5.625, 67)
]
for time, pitch in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, unique chords each bar, comp on 2 and 4
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Dm7 (D, F, A, C)

# Bar 2: F7 (1.5s)
piano_notes = [
    (1.5, 71), (1.5, 74), (1.5, 76), (1.5, 79),  # F, A, C, E
    # Bar 3: Bb7 (3.0s)
    (3.0, 70), (3.0, 73), (3.0, 76), (3.0, 78),  # Bb, D, F, Ab
    # Bar 4: Dm7 (4.5s)
    (4.5, 72), (4.5, 74), (4.5, 77), (4.5, 79)   # D, F, A, C
]
for time, pitch in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(piano_note)

# Sax: Motif starts on 1.5s — a short, lyrical phrase that lingers
# Motif: F (1.5s), Ab (1.875s), D (2.25s), F (2.625s) — a question
# Then at 4.5s, return to F, but with a twist: C (4.875s), D (5.25s), F (5.625s) — the answer
sax_notes = [
    (1.5, 71), (1.875, 74), (2.25, 77), (2.625, 71),  # Question
    (4.5, 71), (4.875, 76), (5.25, 77), (5.625, 71)   # Answer
]
for time, pitch in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(sax_note)

# Bar 3 and 4: Drums continue with the same pattern
# Bar 2: 1.5 to 3.0s
# Bar 3: 3.0 to 4.5s
# Bar 4: 4.5 to 6.0s

# Bar 3: Kick on 1 and 3, snare on 2 and 4
# Time: 3.0 to 4.5s
drum_notes = [
    (3.0, drum_kick), (3.375, drum_hihat), (3.75, drum_kick), (3.75, drum_snare),
    (4.125, drum_hihat), (4.5, drum_kick), (4.5, drum_snare)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 4: Kick on 1 and 3, snare on 2 and 4
# Time: 4.5 to 6.0s
drum_notes = [
    (4.5, drum_kick), (4.875, drum_hihat), (5.25, drum_kick), (5.25, drum_snare),
    (5.625, drum_hihat), (6.0, drum_kick), (6.0, drum_snare)
]
for time, note in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
