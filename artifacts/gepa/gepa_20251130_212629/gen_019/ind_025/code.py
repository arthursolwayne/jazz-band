
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key signature (D major)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0.0)]  # D major

# Define the time per bar (1.5 seconds for 160 BPM, 4/4 time)
time_per_beat = 60.0 / 160.0  # 0.375 seconds per beat
time_per_bar = 4 * time_per_beat  # 1.5 seconds per bar

# ----------------------------
# 1. Drums (Little Ray)
# ----------------------------
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drums_program)

# Bar 1: Kick on beat 1, snare on beat 3, hihat on 2 & 4
kick_time = 0.0
snare_time = 3 * time_per_beat
hihat_time = 2 * time_per_beat
hihat_time2 = 4 * time_per_beat

# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1))

# Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1))

# Hihat on 2 & 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time2, end=hihat_time2 + 0.05))

pm.instruments.append(drums)

# ----------------------------
# 2. Piano (Diane)
# ----------------------------
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

# Bar 2: 7th chords on beat 2 and 4, chromatic, unresolved
# D7 = D F# A C (but we'll use F# and Bb for tension)
# Use D7#9: D F# A C Bb (chromatically shifting)

# Bar 2, beat 2: D7#9 chord (F#, A, C, Bb)
note_times = [2 * time_per_beat]
notes = [63, 66, 67, 69]  # F#, A, C, Bb

for note in notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=note_times[0], end=note_times[0] + 0.2))

# Bar 2, beat 4: same chord, but with a slight delay
note_times = [4 * time_per_beat]
notes = [63, 66, 67, 69]

for note in notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=note_times[0], end=note_times[0] + 0.2))

pm.instruments.append(piano)

# ----------------------------
# 3. Bass (Marcus)
# ----------------------------
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

# Bar 3: Walking bass line with chromatic approach to D, ends on Bb
# Root motion: C# -> D -> Bb (chromatic approach, then tension)

# Bar 3, beat 1: C#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=3 * time_per_beat, end=3 * time_per_beat + 0.2))

# Bar 3, beat 2: D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=4 * time_per_beat, end=4 * time_per_beat + 0.2))

# Bar 3, beat 3: Bb
bass.notes.append(pretty_midi.Note(velocity=90, pitch=44, start=5 * time_per_beat, end=5 * time_per_beat + 0.2))

# Bar 3, beat 4: C# again (chromatic return)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=47, start=6 * time_per_beat, end=6 * time_per_beat + 0.2))

pm.instruments.append(bass)

# ----------------------------
# 4. Tenor Sax (You)
# ----------------------------
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# Bar 4: Melody — a question, not a statement
# D -> F# -> A -> rest — leave it hanging

# Bar 4, beat 1: D (note 62)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=6 * time_per_beat, end=6 * time_per_beat + 0.2))

# Bar 4, beat 2: F# (note 64)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=7 * time_per_beat, end=7 * time_per_beat + 0.2))

# Bar 4, beat 3: A (note 65)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=8 * time_per_beat, end=8 * time_per_beat + 0.2))

# Bar 4, beat 4: No note — silence, a question

pm.instruments.append(sax)

# Save the MIDI file
pm.write('jazz_intro_wayne_shorter.mid')
