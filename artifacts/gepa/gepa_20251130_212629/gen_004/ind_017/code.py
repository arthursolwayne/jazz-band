
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # 480 ticks per quarter note

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempos = [pretty_midi.TempoChange(160.0, 0.0)]

# Define instruments
# Tenor Sax (program 64)
sax_program = pretty_midi.Instrument(program=64)
pm.instruments.append(sax_program)

# Bass (program 33)
bass_program = pretty_midi.Instrument(program=33)
pm.instruments.append(bass_program)

# Piano (program 0)
piano_program = pretty_midi.Instrument(program=0)
pm.instruments.append(piano_program)

# Drums (program 128)
drum_program = pretty_midi.Instrument(program=128)
pm.instruments.append(drum_program)

# Tempo: 160 BPM => 0.375 seconds per beat
# Bar = 1.5 seconds

# BAR 1: Little Ray on drums — kick on 1 and 3, snare on 2 and 4
# Define drum notes
drum_kick = 36  # MIDI note for kick
drum_snare = 38  # MIDI note for snare
drum_hihat = 42  # MIDI note for closed hihat

# Time for bar 1: 0.0 to 1.5 seconds
# Each beat is 0.375 seconds, so 4 beats per bar

# Kick on 1 and 3
drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=drum_kick, start=0.0, end=0.375))
drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=drum_kick, start=0.75, end=1.125))

# Snare on 2 and 4
drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=drum_snare, start=0.375, end=0.75))
drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=drum_snare, start=1.125, end=1.5))

# Hihat on every eighth note
for i in range(8):
    start_time = i * 0.1875
    drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=drum_hihat, start=start_time, end=start_time + 0.1875))

# BAR 2: Saxophone enters with a short motif in Fm (F, Ab, Bb, D)
# Time: 1.5 to 3.0 seconds

# Fm7 chord: F, Ab, Bb, C
# Fm7 in Fm (root is F, 7th is C)

# Motif: F (Ab), Bb (D), C, Ab (F)
# Notes in Fm (F, Ab, Bb, C)

# Start at 1.5 seconds
note_lengths = 0.375
note_times = [1.5, 1.875, 2.25, 2.625]

# Notes: F, Ab, Bb, D
# MIDI notes: 65 (F), 68 (Ab), 70 (Bb), 72 (C), 74 (D)
# F is 65, Ab is 68, Bb is 70, D is 74

sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875))  # Ab
sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25))  # Bb
sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625))  # C
sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0))   # Ab

# BAR 3: Bass enters with walking line (chromatic approach)
# Time: 1.5 to 3.0 seconds

# Fm7 walking line: F, Gb, Ab, Bb, B, C, D, Eb, etc.
# F = 65, Gb = 66, Ab = 68, Bb = 70, B = 71, C = 72, D = 74, Eb = 73

# Walking line: F, Gb, Ab, Bb over the first bar
# Time: 1.5 to 3.0 seconds

bass_notes = [
    (65, 1.5, 1.875),  # F
    (66, 1.875, 2.25), # Gb
    (68, 2.25, 2.625), # Ab
    (70, 2.625, 3.0)   # Bb
]

for pitch, start, end in bass_notes:
    bass_program.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# BAR 3: Piano enters with 7th chords on 2 and 4 (comping)
# Time: 1.5 to 3.0 seconds

# Fm7 on 2 and 4
# Fm7 = F, Ab, Bb, C (F is root, 7th is C)
# On 2 and 4

# 2nd beat (1.875) and 4th beat (3.0)

# Fm7 chord: F (65), Ab (68), Bb (70), C (72)

# Play on 2 and 4, with 1/2 note duration
piano_notes = [
    (65, 1.875, 2.25),
    (68, 1.875, 2.25),
    (70, 1.875, 2.25),
    (72, 1.875, 2.25),
    (65, 3.0, 3.375),
    (68, 3.0, 3.375),
    (70, 3.0, 3.375),
    (72, 3.0, 3.375)
]

for pitch, start, end in piano_notes:
    piano_program.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# BAR 4: Sax completes the motif — hangs on the last note (Ab)
# Time: 3.0 to 3.375 seconds

# Motif: F, Ab, Bb, D
# Repeat Ab as a resolution

sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375))

# Save MIDI
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
