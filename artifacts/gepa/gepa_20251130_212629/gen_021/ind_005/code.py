
import pretty_midi
from pretty_midi import Note, Instrument

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# MIDI note numbers for F minor scale (C4 = 60)
# F = 65, Gb = 66, Ab = 67, Bb = 68, B = 69, Db = 70, Eb = 71

# Define the tempo
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Electric Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI uses piano for drums

# Add instruments
bass_instrument = Instrument(program=bass_program)
piano_instrument = Instrument(program=piano_program)
sax_instrument = Instrument(program=sax_program)
drum_instrument = Instrument(program=drum_program)

pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(sax_instrument)
pm.instruments.append(drum_instrument)

# Time per beat (seconds)
beat = 60.0 / 160  # 0.375 seconds per beat
bar = 4 * beat  # 1.5 seconds per bar

# Define bar positions (in seconds)
bar1_start = 0
bar1_end = bar
bar2_start = bar1_end
bar2_end = bar1_end + bar
bar3_start = bar2_end
bar3_end = bar2_end + bar
bar4_start = bar3_end
bar4_end = bar3_end + bar

# -------------------
# DRUMS - Little Ray
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth, but leave last eighth empty

# Kick on 1 and 3 of bar 1
drum_instrument.notes.append(Note(36, 64, bar1_start, bar1_start + beat/4))  # Kick on 1
drum_instrument.notes.append(Note(36, 64, bar1_start + beat*1.5, bar1_start + beat*1.75))  # Kick on 3

# Snare on 2 and 4 of bar 1
drum_instrument.notes.append(Note(38, 64, bar1_start + beat*0.5, bar1_start + beat*0.75))  # Snare on 2
drum_instrument.notes.append(Note(38, 64, bar1_start + beat*1.5, bar1_start + beat*1.75))  # Snare on 4

# Hi-hats on every eighth (but leave the last 8th empty)
for i in range(8):
    if i != 7:
        drum_instrument.notes.append(Note(42, 64, bar1_start + beat * (i / 8), bar1_start + beat * (i / 8) + beat/8))

# Bar 2: Kick, snare, and hihat on every eighth
for i in range(4):
    kick_time = bar2_start + beat * i
    snare_time = kick_time + beat/2
    drum_instrument.notes.append(Note(36, 64, kick_time, kick_time + beat/4))  # Kick
    drum_instrument.notes.append(Note(38, 64, snare_time, snare_time + beat/4))  # Snare
    for j in range(2):
        hihat_time = kick_time + beat * j / 2
        drum_instrument.notes.append(Note(42, 64, hihat_time, hihat_time + beat/8))

# Bar 3: Same as Bar 2
for i in range(4):
    kick_time = bar3_start + beat * i
    snare_time = kick_time + beat/2
    drum_instrument.notes.append(Note(36, 64, kick_time, kick_time + beat/4))  # Kick
    drum_instrument.notes.append(Note(38, 64, snare_time, snare_time + beat/4))  # Snare
    for j in range(2):
        hihat_time = kick_time + beat * j / 2
        drum_instrument.notes.append(Note(42, 64, hihat_time, hihat_time + beat/8))

# Bar 4: Same as Bar 2
for i in range(4):
    kick_time = bar4_start + beat * i
    snare_time = kick_time + beat/2
    drum_instrument.notes.append(Note(36, 64, kick_time, kick_time + beat/4))  # Kick
    drum_instrument.notes.append(Note(38, 64, snare_time, snare_time + beat/4))  # Snare
    for j in range(2):
        hihat_time = kick_time + beat * j / 2
        drum_instrument.notes.append(Note(42, 64, hihat_time, hihat_time + beat/8))

# -------------------
# BASS - Marcus (Walking line, chromatic approaches, no repeated notes)

# Bar 1: Gb, F, Ab, Bb
bass_instrument.notes.append(Note(66, 60, bar1_start, bar1_start + beat/4))  # Gb
bass_instrument.notes.append(Note(65, 60, bar1_start + beat/4, bar1_start + beat/2))  # F
bass_instrument.notes.append(Note(67, 60, bar1_start + beat/2, bar1_start + beat*1.25))  # Ab
bass_instrument.notes.append(Note(68, 60, bar1_start + beat*1.25, bar1_start + beat*1.5))  # Bb

# Bar 2: B, Db, Eb, F
bass_instrument.notes.append(Note(69, 60, bar2_start, bar2_start + beat/4))  # B
bass_instrument.notes.append(Note(70, 60, bar2_start + beat/4, bar2_start + beat/2))  # Db
bass_instrument.notes.append(Note(71, 60, bar2_start + beat/2, bar2_start + beat*1.25))  # Eb
bass_instrument.notes.append(Note(65, 60, bar2_start + beat*1.25, bar2_start + beat*1.5))  # F

# Bar 3: Gb, Ab, B, Db
bass_instrument.notes.append(Note(66, 60, bar3_start, bar3_start + beat/4))  # Gb
bass_instrument.notes.append(Note(67, 60, bar3_start + beat/4, bar3_start + beat/2))  # Ab
bass_instrument.notes.append(Note(69, 60, bar3_start + beat/2, bar3_start + beat*1.25))  # B
bass_instrument.notes.append(Note(70, 60, bar3_start + beat*1.25, bar3_start + beat*1.5))  # Db

# Bar 4: Eb, F, Gb, Ab
bass_instrument.notes.append(Note(71, 60, bar4_start, bar4_start + beat/4))  # Eb
bass_instrument.notes.append(Note(65, 60, bar4_start + beat/4, bar4_start + beat/2))  # F
bass_instrument.notes.append(Note(66, 60, bar4_start + beat/2, bar4_start + beat*1.25))  # Gb
bass_instrument.notes.append(Note(67, 60, bar4_start + beat*1.25, bar4_start + beat*1.5))  # Ab

# -------------------
# PIANO - Diane (7th chords, comp on 2 and 4, not in the way)

# Bar 1: F7 on beat 2 and 4
piano_instrument.notes.append(Note(65, 64, bar1_start + beat*0.5, bar1_start + beat*0.75))  # F
piano_instrument.notes.append(Note(69, 64, bar1_start + beat*0.5, bar1_start + beat*0.75))  # B
piano_instrument.notes.append(Note(68, 64, bar1_start + beat*0.5, bar1_start + beat*0.75))  # Bb
piano_instrument.notes.append(Note(67, 64, bar1_start + beat*0.5, bar1_start + beat*0.75))  # Ab

piano_instrument.notes.append(Note(65, 64, bar1_start + beat*1.5, bar1_start + beat*1.75))  # F
piano_instrument.notes.append(Note(69, 64, bar1_start + beat*1.5, bar1_start + beat*1.75))  # B
piano_instrument.notes.append(Note(68, 64, bar1_start + beat*1.5, bar1_start + beat*1.75))  # Bb
piano_instrument.notes.append(Note(67, 64, bar1_start + beat*1.5, bar1_start + beat*1.75))  # Ab

# Bar 2: Bb7 on beat 2 and 4
piano_instrument.notes.append(Note(68, 64, bar2_start + beat*0.5, bar2_start + beat*0.75))  # Bb
piano_instrument.notes.append(Note(72, 64, bar2_start + beat*0.5, bar2_start + beat*0.75))  # D
piano_instrument.notes.append(Note(71, 64, bar2_start + beat*0.5, bar2_start + beat*0.75))  # C
piano_instrument.notes.append(Note(67, 64, bar2_start + beat*0.5, bar2_start + beat*0.75))  # Ab

piano_instrument.notes.append(Note(68, 64, bar2_start + beat*1.5, bar2_start + beat*1.75))  # Bb
piano_instrument.notes.append(Note(72, 64, bar2_start + beat*1.5, bar2_start + beat*1.75))  # D
piano_instrument.notes.append(Note(71, 64, bar2_start + beat*1.5, bar2_start + beat*1.75))  # C
piano_instrument.notes.append(Note(67, 64, bar2_start + beat*1.5, bar2_start + beat*1.75))  # Ab

# Bar 3: F7 on beat 2 and 4
piano_instrument.notes.append(Note(65, 64, bar3_start + beat*0.5, bar3_start + beat*0.75))  # F
piano_instrument.notes.append(Note(69, 64, bar3_start + beat*0.5, bar3_start + beat*0.75))  # B
piano_instrument.notes.append(Note(68, 64, bar3_start + beat*0.5, bar3_start + beat*0.75))  # Bb
piano_instrument.notes.append(Note(67, 64, bar3_start + beat*0.5, bar3_start + beat*0.75))  # Ab

piano_instrument.notes.append(Note(65, 64, bar3_start + beat*1.5, bar3_start + beat*1.75))  # F
piano_instrument.notes.append(Note(69, 64, bar3_start + beat*1.5, bar3_start + beat*1.75))  # B
piano_instrument.notes.append(Note(68, 64, bar3_start + beat*1.5, bar3_start + beat*1.75))  # Bb
piano_instrument.notes.append(Note(67, 64, bar3_start + beat*1.5, bar3_start + beat*1.75))  # Ab

# Bar 4: Bb7 on beat 2 and 4
piano_instrument.notes.append(Note(68, 64, bar4_start + beat*0.5, bar4_start + beat*0.75))  # Bb
piano_instrument.notes.append(Note(72, 64, bar4_start + beat*0.5, bar4_start + beat*0.75))  # D
piano_instrument.notes.append(Note(71, 64, bar4_start + beat*0.5, bar4_start + beat*0.75))  # C
piano_instrument.notes.append(Note(67, 64, bar4_start + beat*0.5, bar4_start + beat*0.75))  # Ab

piano_instrument.notes.append(Note(68, 64, bar4_start + beat*1.5, bar4_start + beat*1.75))  # Bb
piano_instrument.notes.append(Note(72, 64, bar4_start + beat*1.5, bar4_start + beat*1.75))  # D
piano_instrument.notes.append(Note(71, 64, bar4_start + beat*1.5, bar4_start + beat*1.75))  # C
piano_instrument.notes.append(Note(67, 64, bar4_start + beat*1.5, bar4_start + beat*1.75))  # Ab

# -------------------
# TENOR SAX - You: A lyrical motif that starts, hangs, and ends unresolved

# Motif: F, Ab, Bb, B — unresolved ending (F -> Ab -> Bb -> B)
note_f = 65
note_ab = 67
note_bb = 68
note_b = 69

# Bar 2: Start the motif
sax_instrument.notes.append(Note(note_f, 72, bar2_start, bar2_start + beat*0.5))  # F
sax_instrument.notes.append(Note(note_ab, 72, bar2_start + beat*0.5, bar2_start + beat*1.0))  # Ab
sax_instrument.notes.append(Note(note_bb, 72, bar2_start + beat*1.0, bar2_start + beat*1.5))  # Bb

# Bar 3: Continue the motif with a slight resolution to B
sax_instrument.notes.append(Note(note_b, 72, bar3_start, bar3_start + beat*0.5))  # B
sax_instrument.notes.append(Note(note_f, 72, bar3_start + beat*0.5, bar3_start + beat*1.0))  # F
sax_instrument.notes.append(Note(note_ab, 72, bar3_start + beat*1.0, bar3_start + beat*1.5))  # Ab

# Bar 4: End with B, unresolved
sax_instrument.notes.append(Note(note_b, 72, bar4_start, bar4_start + beat*0.5))  # B
sax_instrument.notes.append(Note(note_f, 72, bar4_start + beat*0.5, bar4_start + beat*1.0))  # F
sax_instrument.notes.append(Note(note_ab, 72, bar4_start + beat*1.0, bar4_start + beat*1.5))  # Ab

# -------------------
# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file written as 'dante_intro.mid'")
