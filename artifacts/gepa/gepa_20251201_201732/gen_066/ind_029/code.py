
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key signature (F major)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F major is key number 5

# Define the duration of each bar (1.5 seconds at 160 BPM)
bar_duration = 1.5
note_duration = 0.375  # 1/4 note at 160 BPM

# Define the time for each bar
bar_times = [0, bar_duration, bar_duration * 2, bar_duration * 3, bar_duration * 4]

# --------------------
# 1. Drums (Little Ray) - Bar 1: Alone
# --------------------

# Create a drum track
drum_program = pretty_midi.instrument_name_to_program('Drums')
drum_instrument = pretty_midi.Instrument(program=drum_program)

# Kick on 1 and 3
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=note_duration))
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_duration * 1, end=bar_duration * 1 + note_duration))

# Snare on 2 and 4
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_duration * 0.5, end=bar_duration * 0.5 + note_duration))
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_duration * 1.5, end=bar_duration * 1.5 + note_duration))

# Hi-hat on every eighth note
for i in range(0, 4):
    drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * note_duration, end=i * note_duration + note_duration))

pm.instruments.append(drum_instrument)

# --------------------
# 2. Bass (Marcus) - Bars 1-4
# --------------------

# F major scale: F, G, A, Bb, C, D, E
# Walking bass line (roots and fifths with chromatic approaches)
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)

# Bar 1
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=0, end=note_duration))        # F (root)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=note_duration, end=note_duration * 2))  # C (fifth, chromatic down)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=note_duration * 2, end=note_duration * 3))  # G (root)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=note_duration * 3, end=note_duration * 4))  # D (fifth)

# Bar 2 (F7: F, A, C, Eb)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_duration, end=bar_duration + note_duration))      # F
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_duration + note_duration, end=bar_duration + note_duration * 2))  # Ab (chromatic up)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_duration + note_duration * 2, end=bar_duration + note_duration * 3))  # G
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=bar_duration + note_duration * 3, end=bar_duration + note_duration * 4))  # C

# Bar 3 (Bb7: Bb, D, F, Ab)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=bar_duration * 2, end=bar_duration * 2 + note_duration))  # Bb
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_duration * 2 + note_duration, end=bar_duration * 2 + note_duration * 2))  # C (chromatic up)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=bar_duration * 2 + note_duration * 2, end=bar_duration * 2 + note_duration * 3))  # Bb
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_duration * 2 + note_duration * 3, end=bar_duration * 2 + note_duration * 4))  # Ab

# Bar 4 (F7 again, leading to the melody)
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_duration * 3, end=bar_duration * 3 + note_duration))  # F
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_duration * 3 + note_duration, end=bar_duration * 3 + note_duration * 2))  # Ab
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_duration * 3 + note_duration * 2, end=bar_duration * 3 + note_duration * 3))  # G
bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=bar_duration * 3 + note_duration * 3, end=bar_duration * 3 + note_duration * 4))  # C

pm.instruments.append(bass_instrument)

# --------------------
# 3. Piano (Diane) - Bars 2-4
# --------------------

# Open voicings, resolve on the last chord of each bar
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano_instrument = pretty_midi.Instrument(program=piano_program)

# Bar 2 (F7)
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar_duration, end=bar_duration + note_duration))  # F (root)
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar_duration, end=bar_duration + note_duration))  # A
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=bar_duration, end=bar_duration + note_duration))  # C
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar_duration, end=bar_duration + note_duration))  # Eb

# Bar 3 (Bb7)
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar_duration * 2, end=bar_duration * 2 + note_duration))  # Bb
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar_duration * 2, end=bar_duration * 2 + note_duration))  # D
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar_duration * 2, end=bar_duration * 2 + note_duration))  # F
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar_duration * 2, end=bar_duration * 2 + note_duration))  # Ab

# Bar 4 (F7 again)
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=bar_duration * 3, end=bar_duration * 3 + note_duration))  # F
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar_duration * 3, end=bar_duration * 3 + note_duration))  # A
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=bar_duration * 3, end=bar_duration * 3 + note_duration))  # C
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar_duration * 3, end=bar_duration * 3 + note_duration))  # Eb

pm.instruments.append(piano_instrument)

# --------------------
# 4. Tenor Sax (You) - Bars 2-4
# --------------------

# Tenor sax in F (concert F, transposed Bb)
tenor_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
tenor_instrument = pretty_midi.Instrument(program=tenor_program)

# Motif: F - Bb - D - F (suspended feel, descending)
# Bar 2: Start the motif
tenor_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_duration, end=bar_duration + note_duration))  # F
tenor_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar_duration + note_duration * 1.5, end=bar_duration + note_duration * 2.5))  # Bb (delayed, creates tension)

# Bar 3: Continue the motif
tenor_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar_duration * 2, end=bar_duration * 2 + note_duration))  # D
tenor_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_duration * 2 + note_duration * 1.5, end=bar_duration * 2 + note_duration * 2.5))  # F (resolve)

# Bar 4: Return to F and leave it hanging
tenor_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_duration * 3, end=bar_duration * 3 + note_duration))  # F (start of motif)
tenor_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar_duration * 3 + note_duration, end=bar_duration * 3 + note_duration * 1.5))  # Bb (left hanging, tension)

pm.instruments.append(tenor_instrument)

# Save the MIDI file
pm.write('jazz_intro.mid')
