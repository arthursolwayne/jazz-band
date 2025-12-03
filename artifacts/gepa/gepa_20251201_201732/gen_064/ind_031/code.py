
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define tempo (160 BPM)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key: D major
# D = MIDI note 62

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Bass (Marcus)
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# Piano (Diane)
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# Drums (Little Ray)
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

# Sax (You)
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# Define time per bar (160 BPM => 60 / 160 = 0.375 seconds per beat, 1.5 seconds per bar)
bar_time = 1.5

# BAR 1: Drums only — set it up
# Kick on 1, 3 | Snare on 2, 4 | Hihat on every eighth
for bar in range(1):
    time = bar * bar_time
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 1.125)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.375, end=time + 0.75)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.75, end=time + 1.125)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.extend([kick, snare, hihat])

# BAR 2: Everyone in — Sax melody
# You: One short motif — let the space speak
# D (62) -> F# (66) -> A (69) -> D (62) -> space -> D (62) -> F# (66) -> A (69) -> D (62)

note_d = 62
note_fsharp = 66
note_a = 69

# First note: D
sax_note = pretty_midi.Note(velocity=100, pitch=note_d, start=bar_time, end=bar_time + 0.375)
sax.notes.append(sax_note)

# Second note: F#
sax_note = pretty_midi.Note(velocity=100, pitch=note_fsharp, start=bar_time + 0.75, end=bar_time + 1.125)
sax.notes.append(sax_note)

# Third note: A
sax_note = pretty_midi.Note(velocity=100, pitch=note_a, start=bar_time + 1.125, end=bar_time + 1.5)
sax.notes.append(sax_note)

# Bars 2-4: Bass, Piano, and Drums continue

# Bass (Marcus): Walking line with chromatic approach
# Bar 2: D2 (38), chromatic app. to G2 (43)
# Bar 3: G2 (43), chromatic app. to D2 (38)
# Bar 4: D2 (38), chromatic app. to G2 (43)

# Bar 2 (time = 1.5)
bass_note = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + 0.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.5 + 0.375)
bass.notes.append(bass_note)

# Bar 3 (time = 3.0)
bass_note = pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.0 + 0.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.0 + 0.375)
bass.notes.append(bass_note)

# Bar 4 (time = 4.5)
bass_note = pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.5 + 0.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=39, start=4.5, end=4.5 + 0.375)
bass.notes.append(bass_note)

# Piano (Diane): Open voicings, different chords each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
# Bar 3: G7sus4 (G, C, D, F)
# Bar 4: Am7 (A, C, E, G)

# Bar 2: Dmaj7
note_d = 62
note_fs = 66
note_a = 69
note_cs = 67
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_d, start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_fs, start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_a, start=1.5, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_cs, start=1.5, end=1.5 + 0.375))

# Bar 3: G7sus4
note_g = 67
note_c = 60
note_d = 62
note_f = 58
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_g, start=3.0, end=3.0 + 0.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_c, start=3.0, end=3.0 + 0.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_d, start=3.0, end=3.0 + 0.75))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_f, start=3.0, end=3.0 + 0.75))

# Bar 4: Am7
note_a = 69
note_c = 60
note_e = 64
note_g = 67
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_a, start=4.5, end=4.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_c, start=4.5, end=4.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_e, start=4.5, end=4.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=note_g, start=4.5, end=4.5 + 0.375))

# BAR 3 & 4: Drums continue with same pattern
for bar in range(2, 4):  # bar 2 and 3
    time = bar * bar_time
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 1.125)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.375, end=time + 0.75)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 0.75, end=time + 1.125)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.extend([kick, snare, hihat])

# Save the MIDI file
pm.write("dante_intro.mid")

print("Generated: 'dante_intro.mid' — ready to play.")
