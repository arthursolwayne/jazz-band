
import pretty_midi

# Initialize the MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note numbers
# Drums: kick=36, snare=38, hihat=42
# Bass: D2 = 38, G2 = 43, etc.
# Piano: Fm7 = [F, Ab, C, Eb] = [53, 60, 65, 67] for root position
# Sax: melody to be defined

# ---------------------------- BAR 1: DRUMS ONLY (0.0 - 1.5s) ----------------------------
# Little Ray hits kick on 1 and 3, snare on 2 and 4, hihat every eighth

# Define the pattern (0.375s per beat)
bar_length = 1.5
beat_length = bar_length / 4

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625))  # End slightly beyond bar

# Hihat on every eighth note (16 notes per bar)
for i in range(8):
    start = i * beat_length
    end = start + beat_length / 2
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# ---------------------------- BAR 2: FULL QUARTET (1.5 - 3.0s) ----------------------------
# Time starts at 1.5s

# Bass: Marcus on walking line - D2 (38), G2 (43), chromatic approaches
bass_notes = [
    (38, 1.5, 1.625),     # D2
    (40, 1.625, 1.75),    # Eb2 (chromatic approach)
    (43, 1.75, 1.875),    # G2
    (42, 1.875, 2.0),     # F2 (chromatic approach)
    (38, 2.0, 2.125),     # D2
    (40, 2.125, 2.25),    # Eb2
    (43, 2.25, 2.375),    # G2
    (42, 2.375, 2.5),     # F2
    (38, 2.5, 2.625),     # D2
    (40, 2.625, 2.75),    # Eb2
    (43, 2.75, 2.875),    # G2
    (42, 2.875, 3.0),     # F2
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Diane - Open voicings, different chords each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb) → root position
piano_notes = [
    (53, 1.5, 3.0),  # F
    (60, 1.5, 3.0),  # Ab
    (65, 1.5, 3.0),  # C
    (67, 1.5, 3.0)   # Eb
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Dante - One short motif, start it, leave it hanging, come back and finish
# Motif: F (60) → Ab (62) → F (60) → Ab (62) → C (65)
# Start on 1.5, play first two notes, then wait until 2.5 to finish
sax_notes = [
    (60, 1.5, 1.625),  # F
    (62, 1.625, 1.75), # Ab
    (60, 2.5, 2.625),  # F (delayed)
    (62, 2.625, 2.75), # Ab
    (65, 2.75, 2.875)  # C
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# ---------------------------- BAR 3: FULL QUARTET (3.0 - 4.5s) ----------------------------
# Bass: Marcus - Walking line again, D2 (38), G2 (43), chromatic approaches
bass_notes = [
    (38, 3.0, 3.125),     # D2
    (40, 3.125, 3.25),    # Eb2
    (43, 3.25, 3.375),    # G2
    (42, 3.375, 3.5),     # F2
    (38, 3.5, 3.625),     # D2
    (40, 3.625, 3.75),    # Eb2
    (43, 3.75, 3.875),    # G2
    (42, 3.875, 4.0),     # F2
    (38, 4.0, 4.125),     # D2
    (40, 4.125, 4.25),    # Eb2
    (43, 4.25, 4.375),    # G2
    (42, 4.375, 4.5),     # F2
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Diane - Different chord each bar, resolve on last
# Bar 3: Bbmaj7 (Bb, D, F, Ab) → root position
piano_notes = [
    (57, 3.0, 4.5),  # Bb
    (62, 3.0, 4.5),  # D
    (65, 3.0, 4.5),  # F
    (60, 3.0, 4.5)   # Ab
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Dante - Play the motif again, but change the last note
# Motif: F (60) → Ab (62) → F (60) → Ab (62) → E (64)
sax_notes = [
    (60, 3.0, 3.125),  # F
    (62, 3.125, 3.25), # Ab
    (60, 3.25, 3.375), # F
    (62, 3.375, 3.5),  # Ab
    (64, 3.5, 3.625)   # E
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# ---------------------------- BAR 4: FULL QUARTET (4.5 - 6.0s) ----------------------------
# Bass: Marcus - Walking line again, D2 (38), G2 (43), chromatic
bass_notes = [
    (38, 4.5, 4.625),     # D2
    (40, 4.625, 4.75),    # Eb2
    (43, 4.75, 4.875),    # G2
    (42, 4.875, 5.0),     # F2
    (38, 5.0, 5.125),     # D2
    (40, 5.125, 5.25),    # Eb2
    (43, 5.25, 5.375),    # G2
    (42, 5.375, 5.5),     # F2
    (38, 5.5, 5.625),     # D2
    (40, 5.625, 5.75),    # Eb2
    (43, 5.75, 5.875),    # G2
    (42, 5.875, 6.0),     # F2
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Diane - Different chord each bar, resolve on last
# Bar 4: G7 (G, B, D, F) → root position
piano_notes = [
    (67, 4.5, 6.0),  # G
    (71, 4.5, 6.0),  # B
    (69, 4.5, 6.0),  # D
    (65, 4.5, 6.0)   # F
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Dante - Finish the motif, maybe a run up to G (67)
sax_notes = [
    (60, 4.5, 4.625),  # F
    (62, 4.625, 4.75), # Ab
    (60, 4.75, 4.875), # F
    (62, 4.875, 5.0),  # Ab
    (65, 5.0, 5.125),  # C
    (62, 5.125, 5.25), # Ab
    (65, 5.25, 5.375), # C
    (67, 5.375, 5.5),  # G
    (65, 5.5, 5.625),  # C
    (62, 5.625, 5.75), # Ab
    (65, 5.75, 5.875), # C
    (67, 5.875, 6.0)   # G
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
