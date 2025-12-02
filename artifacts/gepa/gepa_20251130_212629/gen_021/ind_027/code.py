
import pretty_midi
from pretty_midi import Note, Instrument

# Settings
tempo = 160  # BPM
time_signature = (4, 4)
key = 'F major'
duration = 6.0  # seconds for 4 bars
beat = 0.375  # seconds per beat at 160 BPM
bar_length = 1.5  # seconds per bar

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Acoustic Drum Kit
bass = pretty_midi.Instrument(program=33)   # Electric Bass
piano = pretty_midi.Instrument(program=0)   # Acoustic Grand Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Saxophone

# Add instruments to MIDI
midi.instruments.append(drums)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Start time: 0 seconds

# --- Bar 1: Little Ray (Drums) alone ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 to 1.5 seconds
# Kick on 1 (0.0) and 3 (1.125)
kick_1 = Note(36, 100, 0.0, 0.2)
kick_3 = Note(36, 100, 1.125, 0.2)

# Snare on 2 (0.75) and 4 (1.5)
snare_2 = Note(38, 100, 0.75, 0.2)
snare_4 = Note(38, 100, 1.5, 0.2)

# Hihat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5)
hihat_1 = Note(42, 90, 0.0, 0.1)
hihat_2 = Note(42, 90, 0.375, 0.1)
hihat_3 = Note(42, 90, 0.75, 0.1)
hihat_4 = Note(42, 90, 1.125, 0.1)
hihat_5 = Note(42, 90, 1.5, 0.1)

drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4, hihat_5])

# --- Bar 2: Everyone enters --- 
# Bar 2: 1.5 to 3.0 seconds

# Marcus on bass: Walking line, chromatic approaches, no repeating notes
# F major scale: F, G, A, Bb, B, C, D, F
# Walking line: F, G, Ab, Bb, B, C, D, Eb

bass_notes = [
    Note(70, 75, 1.5, 0.375),  # F (70)
    Note(71, 75, 1.875, 0.375),  # G (71)
    Note(69, 75, 2.25, 0.375),  # Ab (69)
    Note(70, 75, 2.625, 0.375),  # Bb (70)
    Note(71, 75, 2.999, 0.375),  # B (71)
    Note(72, 75, 3.375, 0.375),  # C (72)
    Note(74, 75, 3.75, 0.375),   # D (74)
    Note(68, 75, 4.125, 0.375)   # Eb (68)
]

bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4 (beat 2 and 4 of bar 2)

# Bar 2 is 1.5 to 3.0
# Beat 2: 1.875
# Beat 4: 3.0
# F7 = F, A, C, Eb
# Bb7 = Bb, D, F, Ab

# F7 at 1.875
note_f = Note(70, 80, 1.875, 0.1)
note_a = Note(72, 80, 1.875, 0.1)
note_c = Note(74, 80, 1.875, 0.1)
note_eb = Note(68, 80, 1.875, 0.1)

# Bb7 at 3.0
note_bb = Note(70, 80, 3.0, 0.1)
note_d = Note(74, 80, 3.0, 0.1)
note_f = Note(76, 80, 3.0, 0.1)
note_ab = Note(69, 80, 3.0, 0.1)

piano.notes.extend([note_f, note_a, note_c, note_eb, note_bb, note_d, note_f, note_ab])

# Little Ray: Kick on 1 (3.0), snare on 2 (3.375), hihat on every eighth

kick_1 = Note(36, 100, 3.0, 0.2)
snare_2 = Note(38, 100, 3.375, 0.2)
hihat_1 = Note(42, 90, 3.0, 0.1)
hihat_2 = Note(42, 90, 3.375, 0.1)
hihat_3 = Note(42, 90, 3.75, 0.1)
hihat_4 = Note(42, 90, 4.125, 0.1)
hihat_5 = Note(42, 90, 4.5, 0.1)

drums.notes.extend([kick_1, snare_2, hihat_1, hihat_2, hihat_3, hihat_4, hihat_5])

# --- Bar 3: You (Sax) take the melody --- 
# Start on F, then a chromatic run up to G, then resolve to Bb

# Bar 3: 3.0 to 4.5 seconds
# F (74) at beat 1 (3.0)
# Chromatic run: F, F#, G (74, 75, 76)
# Then rest for a beat
# Then resolve to Bb (72)

# F (tenor sax is transposed, F on sax is Bb in concert)
note_f = Note(74, 100, 3.0, 0.2)
note_fs = Note(75, 100, 3.375, 0.2)
note_g = Note(76, 100, 3.75, 0.2)
note_rest = Note(74, 0, 4.125, 0.375)
note_bb = Note(72, 100, 4.5, 0.2)

sax.notes.extend([note_f, note_fs, note_g, note_rest, note_bb])

# --- Bar 4: Continue with the motif, resolve with a rest or space ---

# Bar 4: 4.5 to 6.0 seconds
# Repeat the motif with dynamic control

# F (Bb in concert) again, softer
note_f = Note(74, 80, 4.5, 0.2)
note_fs = Note(75, 80, 4.875, 0.2)
note_g = Note(76, 80, 5.25, 0.2)
note_rest = Note(74, 0, 5.625, 0.375)

sax.notes.extend([note_f, note_fs, note_g, note_rest])

# Save MIDI file
midi.write('4_bar_intro.midi')
