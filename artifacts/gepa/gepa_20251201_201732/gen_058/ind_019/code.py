
import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor
key = 'F minor'

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

# Add the time signature
midi.time_signature_changes.append(time_signature)

# Define the tempo (beats per minute)
midi.tempo_changes.append(pretty_midi.TempoChange(160, 0))

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Function to create a note
def create_note(note_number, start, end, velocity):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)
    return note

# --- BAR 1: DRUMS ALONE (Little Ray) ---
# Bar 1 = 1.5 seconds

# Kick on 1 and 3
kick_1 = create_note(36, 0.0, 0.25, 100)
kick_3 = create_note(36, 0.75, 0.99, 100)

# Snare on 2 and 4
snare_2 = create_note(38, 0.5, 0.7, 100)
snare_4 = create_note(38, 1.0, 1.2, 100)

# Hi-hat on every eighth
hihat_notes = [create_note(42, i * 0.375, i * 0.375 + 0.1, 100) for i in range(4)]
hihat_notes += [create_note(42, i * 0.375, i * 0.375 + 0.1, 100) for i in range(4, 8)]

# Add to drums
drums.notes.extend([kick_1, kick_3, snare_2, snare_4] + hihat_notes)
midi.instruments.append(drums)

# --- BAR 2-4: EVERYONE IN ---
# Duration: 3 seconds
# Each bar is 1.5 seconds

# Time for Bar 2: 1.5s
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# --- BASS LINE (Marcus) ---
# Walking line, roots and fifths with chromatic approaches
# F minor: F, G#, A, Bb, C, Db, D, Eb

# Bar 2: F - G# (chromatic approach) - A - Bb
note_f = create_note(65, bar2_start, bar2_start + 0.1, 70)
note_gsh = create_note(67, bar2_start + 0.1, bar2_start + 0.2, 60)
note_a = create_note(69, bar2_start + 0.2, bar2_start + 0.3, 70)
note_bb = create_note(67, bar2_start + 0.3, bar2_start + 0.35, 60)

# Bar 3: C - Db (chromatic approach) - D - Eb
note_c = create_note(60, bar3_start, bar3_start + 0.1, 70)
note_db = create_note(61, bar3_start + 0.1, bar3_start + 0.2, 60)
note_d = create_note(62, bar3_start + 0.2, bar3_start + 0.3, 70)
note_eb = create_note(63, bar3_start + 0.3, bar3_start + 0.35, 60)

# Bar 4: F - G# (chromatic approach) - A - Bb (resolve on Bb)
note_f2 = create_note(65, bar4_start, bar4_start + 0.1, 70)
note_gsh2 = create_note(67, bar4_start + 0.1, bar4_start + 0.2, 60)
note_a2 = create_note(69, bar4_start + 0.2, bar4_start + 0.3, 70)
note_bb2 = create_note(67, bar4_start + 0.3, bar4_start + 0.35, 60)

# Add to bass
bass.notes.extend([note_f, note_gsh, note_a, note_bb, note_c, note_db, note_d, note_eb, note_f2, note_gsh2, note_a2, note_bb2])
midi.instruments.append(bass)

# --- PIANO (Diane) ---
# Open voicings, different chord each bar, resolve on the last

# Bar 2: F7#9 (F, A, C, E, G#, Bb) -> resolve on Bb
note_f_piano = create_note(65, bar2_start, bar2_start + 0.1, 80)
note_a_piano = create_note(69, bar2_start, bar2_start + 0.1, 80)
note_c_piano = create_note(60, bar2_start, bar2_start + 0.1, 80)
note_e_piano = create_note(64, bar2_start, bar2_start + 0.1, 80)
note_gs_piano = create_note(67, bar2_start, bar2_start + 0.1, 80)
note_bb_piano = create_note(67, bar2_start + 0.1, bar2_start + 0.2, 80)

# Bar 3: G#7b9 (G#, B, D, F#, A, C) -> resolve on C
note_gs_piano2 = create_note(67, bar3_start, bar3_start + 0.1, 80)
note_b_piano = create_note(71, bar3_start, bar3_start + 0.1, 80)
note_d_piano = create_note(62, bar3_start, bar3_start + 0.1, 80)
note_fsh_piano = create_note(66, bar3_start, bar3_start + 0.1, 80)
note_a_piano2 = create_note(69, bar3_start, bar3_start + 0.1, 80)
note_c_piano2 = create_note(60, bar3_start + 0.1, bar3_start + 0.2, 80)

# Bar 4: A7#9 (A, C#, E, G#, B, D) -> resolve on D
note_a_piano3 = create_note(69, bar4_start, bar4_start + 0.1, 80)
note_cs_piano = create_note(71, bar4_start, bar4_start + 0.1, 80)
note_e_piano2 = create_note(64, bar4_start, bar4_start + 0.1, 80)
note_gs_piano3 = create_note(67, bar4_start, bar4_start + 0.1, 80)
note_b_piano2 = create_note(71, bar4_start, bar4_start + 0.1, 80)
note_d_piano2 = create_note(62, bar4_start + 0.1, bar4_start + 0.2, 80)

# Add to piano
piano.notes.extend([note_f_piano, note_a_piano, note_c_piano, note_e_piano, note_gs_piano, note_bb_piano,
                    note_gs_piano2, note_b_piano, note_d_piano, note_fsh_piano, note_a_piano2, note_c_piano2,
                    note_a_piano3, note_cs_piano, note_e_piano2, note_gs_piano3, note_b_piano2, note_d_piano2])
midi.instruments.append(piano)

# --- SAX (You) ---
# One short motif, haunting, incomplete, leaves it hanging

# Bar 2: Start with a triplet on F, resolve with G# on beat 2
note_f_sax = create_note(65, bar2_start, bar2_start + 0.2, 110)  # Triplet
note_gs_sax = create_note(67, bar2_start + 0.2, bar2_start + 0.25, 100)  # Beat 2

# Bar 3: Continue with a phrase that feels unresolved
note_gs_sax2 = create_note(67, bar3_start + 0.1, bar3_start + 0.15, 100)
note_a_sax = create_note(69, bar3_start + 0.15, bar3_start + 0.2, 100)
note_bb_sax = create_note(67, bar3_start + 0.2, bar3_start + 0.25, 100)

# Bar 4: Let it rest — leave the ending open
note_rest = create_note(60, bar4_start, bar4_start + 0.2, 0)  # Rest with zero velocity

# Add to sax
sax.notes.extend([note_f_sax, note_gs_sax, note_gs_sax2, note_a_sax, note_bb_sax, note_rest])
midi.instruments.append(sax)

# Save the MIDI file
# midi.write disabled
