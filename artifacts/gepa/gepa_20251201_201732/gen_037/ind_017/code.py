
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each member of the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note numbers
# Drums: kick=36, snare=38, hihat=42
# Bass: D2 (62), G2 (67), chromatic approaches
# Piano: Open voicings on each bar
# Sax: One short motif, start and finish it

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Define time in seconds (each bar is 1.5s at 160 BPM)
bar_length = 1.5
bar_1_start = 0.0
bar_1_end = bar_length

# Add kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start, end=bar_1_start + 0.1)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_1_start + 0.75, end=bar_1_start + 0.85)
drums.notes.append(drum_kick_1)
drums.notes.append(drum_kick_3)

# Add snare on 2 and 4
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + 0.375, end=bar_1_start + 0.475)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_1_start + 0.75, end=bar_1_start + 0.85)
drums.notes.append(drum_snare_2)
drums.notes.append(drum_snare_4)

# Add hihat on every eighth note
for i in range(8):
    start = bar_1_start + i * 0.1875
    end = start + 0.1
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(hihat)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Define the time for bars 2-4
bar_2_start = bar_length
bar_3_start = bar_2_start + bar_length
bar_4_start = bar_3_start + bar_length

# BASS LINE (Marcus): D2 (62), G2 (67), chromatic approaches
# Bar 2: D2 (62), G2 (67), F2 (65), G2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=bar_2_start, end=bar_2_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=67, start=bar_2_start + 0.375, end=bar_2_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=65, start=bar_2_start + 0.75, end=bar_2_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=67, start=bar_2_start + 1.125, end=bar_2_start + 1.5)
]

# Bar 3: G2 (67), A2 (69), G2 (67), F2 (65)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=67, start=bar_3_start, end=bar_3_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=69, start=bar_3_start + 0.375, end=bar_3_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=67, start=bar_3_start + 0.75, end=bar_3_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=65, start=bar_3_start + 1.125, end=bar_3_start + 1.5)
])

# Bar 4: F2 (65), E2 (64), D2 (62), C2 (60)
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=65, start=bar_4_start, end=bar_4_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=64, start=bar_4_start + 0.375, end=bar_4_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=62, start=bar_4_start + 0.75, end=bar_4_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=60, start=bar_4_start + 1.125, end=bar_4_start + 1.5)
])

bass.notes.extend(bass_notes)

# PIANO LINE (Diane): Open voicings, different chords each bar, resolve on last beat

# Bar 2: Fm7 (F, Ab, C, D)
# F (65), Ab (68), C (60), D (62)
note_1 = pretty_midi.Note(velocity=100, pitch=65, start=bar_2_start, end=bar_2_start + 1.5)
note_2 = pretty_midi.Note(velocity=100, pitch=68, start=bar_2_start, end=bar_2_start + 1.5)
note_3 = pretty_midi.Note(velocity=100, pitch=60, start=bar_2_start, end=bar_2_start + 1.5)
note_4 = pretty_midi.Note(velocity=100, pitch=62, start=bar_2_start, end=bar_2_start + 1.5)
piano.notes.extend([note_1, note_2, note_3, note_4])

# Bar 3: Am7 (A, C, E, G)
note_1 = pretty_midi.Note(velocity=100, pitch=69, start=bar_3_start, end=bar_3_start + 1.5)
note_2 = pretty_midi.Note(velocity=100, pitch=60, start=bar_3_start, end=bar_3_start + 1.5)
note_3 = pretty_midi.Note(velocity=100, pitch=64, start=bar_3_start, end=bar_3_start + 1.5)
note_4 = pretty_midi.Note(velocity=100, pitch=67, start=bar_3_start, end=bar_3_start + 1.5)
piano.notes.extend([note_1, note_2, note_3, note_4])

# Bar 4: Dm7 (D, F, A, C)
note_1 = pretty_midi.Note(velocity=100, pitch=62, start=bar_4_start, end=bar_4_start + 1.5)
note_2 = pretty_midi.Note(velocity=100, pitch=65, start=bar_4_start, end=bar_4_start + 1.5)
note_3 = pretty_midi.Note(velocity=100, pitch=69, start=bar_4_start, end=bar_4_start + 1.5)
note_4 = pretty_midi.Note(velocity=100, pitch=60, start=bar_4_start, end=bar_4_start + 1.5)
piano.notes.extend([note_1, note_2, note_3, note_4])

# SAX LINE (Dante): One short motif, start it, leave it hanging, come back and finish it

# Bar 2: Start the motif (F, Ab, G)
note_1 = pretty_midi.Note(velocity=110, pitch=65, start=bar_2_start, end=bar_2_start + 0.375)
note_2 = pretty_midi.Note(velocity=110, pitch=68, start=bar_2_start + 0.375, end=bar_2_start + 0.75)
note_3 = pretty_midi.Note(velocity=110, pitch=67, start=bar_2_start + 0.75, end=bar_2_start + 1.125)
sax.notes.extend([note_1, note_2, note_3])

# Bar 3: Leave it hanging, silence
# No notes

# Bar 4: Come back and finish it (F, Ab, D)
note_1 = pretty_midi.Note(velocity=110, pitch=65, start=bar_4_start, end=bar_4_start + 0.375)
note_2 = pretty_midi.Note(velocity=110, pitch=68, start=bar_4_start + 0.375, end=bar_4_start + 0.75)
note_3 = pretty_midi.Note(velocity=110, pitch=62, start=bar_4_start + 0.75, end=bar_4_start + 1.125)
sax.notes.extend([note_1, note_2, note_3])

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI to disk
# midi.write disabled
