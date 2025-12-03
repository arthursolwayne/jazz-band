
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: Fm (F minor)
# Scale degrees: F, G, Ab, Bb, Bb, C, Db, F
# Root: F (65 Hz), 3rd: Ab (69.3 Hz), 5th: C (65.4 Hz) — but in Fm, the 5th is C, not G.

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key signature: F minor
pm.key_signature_changes = [pretty_midi.KeySignature(4, 0)]  # 4 = F minor

# Define timing
BPM = 160
seconds_per_beat = 60 / BPM
bar_duration = 4 * seconds_per_beat  # 6.0 seconds total

# Create instruments
bass_program = Program(33)  # Electric Bass
piano_program = Program(0)   # Acoustic Piano
drums_program = Program(0)   # Drums
sax_program = Program(64)    # Tenor Saxophone

# Create instruments
bass_instrument = Instrument(bass_program)
piano_instrument = Instrument(piano_program)
drums_instrument = Instrument(drums_program)
sax_instrument = Instrument(sax_program)

pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# --------------------------
# DRUMS: Little Ray — Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1 = 0 to 1.5 seconds
bar1_start = 0
bar1_end = bar_duration / 4  # 1.5 seconds

# Kick on 1 and 3
kicks = [bar1_start, bar1_start + 0.75]
for kick_time in kicks:
    note = Note(35, 100, kick_time, kick_time + 0.1)
    drums_instrument.notes.append(note)

# Snare on 2 and 4
snare_times = [bar1_start + 0.5, bar1_start + 1.0]
for snare_time in snare_times:
    note = Note(38, 100, snare_time, snare_time + 0.1)
    drums_instrument.notes.append(note)

# Hi-hat on every eighth note
for i in range(8):
    time = bar1_start + i * 0.375
    note = Note(42, 100, time, time + 0.05)
    drums_instrument.notes.append(note)

# --------------------------
# BASS: Marcus — Bar 1: Rest. Bar 2-4: Walking line, roots and fifths with chromatic approaches

# Bar 2
bar2_start = bar1_end
bar2_end = bar1_end * 2

# Fm root (F) = MIDI note 65
# C (fifth) = 69.3 Hz → MIDI note 69
# Chromatic approach: F#, Eb (67 and 64)
# Root: F (65), beat 1
note = Note(65, 100, bar2_start, bar2_start + 0.25)
bass_instrument.notes.append(note)

# Chromatic approach up (F#) on beat 2
note = Note(67, 100, bar2_start + 0.5, bar2_start + 0.75)
bass_instrument.notes.append(note)

# Root (F) on beat 3
note = Note(65, 100, bar2_start + 1.0, bar2_start + 1.25)
bass_instrument.notes.append(note)

# Chromatic approach down (Eb) on beat 4
note = Note(64, 100, bar2_start + 1.5, bar2_start + 1.75)
bass_instrument.notes.append(note)

# Bar 3: Bb (MIDI 62) as root (Bb is the 4th in Fm, but it's used for chromatic motion)
note = Note(62, 100, bar2_end, bar2_end + 0.25)
bass_instrument.notes.append(note)

# Ab (MIDI 67) as chromatic approach
note = Note(67, 100, bar2_end + 0.5, bar2_end + 0.75)
bass_instrument.notes.append(note)

# Bb again on beat 3
note = Note(62, 100, bar2_end + 1.0, bar2_end + 1.25)
bass_instrument.notes.append(note)

# Chromatic up to B (MIDI 67) on beat 4
note = Note(67, 100, bar2_end + 1.5, bar2_end + 1.75)
bass_instrument.notes.append(note)

# Bar 4: C (MIDI 69) as root, approaching from B (MIDI 67)
note = Note(67, 100, bar2_end * 2, bar2_end * 2 + 0.25)
bass_instrument.notes.append(note)

note = Note(69, 100, bar2_end * 2 + 0.5, bar2_end * 2 + 0.75)
bass_instrument.notes.append(note)

note = Note(69, 100, bar2_end * 2 + 1.0, bar2_end * 2 + 1.25)
bass_instrument.notes.append(note)

note = Note(69, 100, bar2_end * 2 + 1.5, bar2_end * 2 + 1.75)
bass_instrument.notes.append(note)

# --------------------------
# PIANO: Diane — Open voicings, different chords each bar, resolve on the last

# Bar 1: Rest
# Bar 2: Fm7 (F, Ab, C, Eb)
# F = 65, Ab = 67, C = 69, Eb = 64
bar2_piano_start = bar2_start
note = Note(64, 100, bar2_piano_start + 0.5, bar2_piano_start + 0.75)
piano_instrument.notes.append(note)
note = Note(65, 100, bar2_piano_start + 0.5, bar2_piano_start + 0.75)
piano_instrument.notes.append(note)
note = Note(67, 100, bar2_piano_start + 0.5, bar2_piano_start + 0.75)
piano_instrument.notes.append(note)
note = Note(69, 100, bar2_piano_start + 0.5, bar2_piano_start + 0.75)
piano_instrument.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab)
# Bb = 62, D = 67, F = 65, Ab = 67 (already played)
note = Note(62, 100, bar2_end + 0.5, bar2_end + 0.75)
piano_instrument.notes.append(note)
note = Note(67, 100, bar2_end + 0.5, bar2_end + 0.75)
piano_instrument.notes.append(note)
note = Note(65, 100, bar2_end + 0.5, bar2_end + 0.75)
piano_instrument.notes.append(note)
note = Note(67, 100, bar2_end + 0.5, bar2_end + 0.75)
piano_instrument.notes.append(note)

# Bar 4: Cm7 (C, Eb, G, Bb)
# C = 69, Eb = 64, G = 71, Bb = 62
note = Note(69, 100, bar2_end * 2 + 0.5, bar2_end * 2 + 0.75)
piano_instrument.notes.append(note)
note = Note(64, 100, bar2_end * 2 + 0.5, bar2_end * 2 + 0.75)
piano_instrument.notes.append(note)
note = Note(71, 100, bar2_end * 2 + 0.5, bar2_end * 2 + 0.75)
piano_instrument.notes.append(note)
note = Note(62, 100, bar2_end * 2 + 0.5, bar2_end * 2 + 0.75)
piano_instrument.notes.append(note)

# --------------------------
# SAX: You — Bar 1: Rest. Bar 2-4: One short motif, sing, leave it hanging, come back

sax_start = bar2_start

# Bar 2: F (65) on beat 1, rest on 2, Ab (67) on 3, rest on 4
note = Note(65, 100, sax_start, sax_start + 0.25)
sax_instrument.notes.append(note)
note = Note(67, 100, sax_start + 1.0, sax_start + 1.25)
sax_instrument.notes.append(note)

# Bar 3: C (69) on beat 1, rest on 2, Ab (67) on 3, rest on 4
note = Note(69, 100, sax_start + 1.5, sax_start + 1.75)
sax_instrument.notes.append(note)
note = Note(67, 100, sax_start + 2.5, sax_start + 2.75)
sax_instrument.notes.append(note)

# Bar 4: F (65) on beat 1, rest on 2, Ab (67) on 3 — leave it hanging
note = Note(65, 100, sax_start + 3.0, sax_start + 3.25)
sax_instrument.notes.append(note)
note = Note(67, 100, sax_start + 4.0, sax_start + 4.25)
sax_instrument.notes.append(note)

# Save the MIDI file
pm.write("wayne_intro.mid")
