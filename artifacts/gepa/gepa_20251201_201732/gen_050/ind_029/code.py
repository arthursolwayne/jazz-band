
import pretty_midi

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
time_signature = pretty_midi.TimeSignature(4, 4, 0)
midi.time_signature_changes.append(time_signature)

# Define the key: D minor (Db is the key, but we'll use D for simplicity with flats)
# We'll use D minor, which is D, Eb, F, G, Ab, Bb, C
# But to keep it dark and unresolved, we'll use D minor with some chromaticism

# Define instruments
# 1. Bass (Marcus) - MIDI program 33 (Acoustic Bass)
# 2. Piano (Diane) - MIDI program 0 (Acoustic Grand Piano)
# 3. Drums (Little Ray) - MIDI program 0 (Acoustic Grand Piano; we'll handle percussion)
# 4. Tenor Sax (You) - MIDI program 67 (Tenor Saxophone)

# Create instruments
bass_program = pretty_midi.Instrument(program=33)
piano_program = pretty_midi.Instrument(program=0)
drum_program = pretty_midi.Instrument(program=0)
sax_program = pretty_midi.Instrument(program=67)

# Add instruments to the MIDI file
midi.instruments.append(bass_program)
midi.instruments.append(piano_program)
midi.instruments.append(drum_program)
midi.instruments.append(sax_program)

# Define tempo (160 BPM)
# 60 seconds per minute, 160 BPM => 60/160 = 0.375 seconds per beat
# 4 bars = 6.0 seconds total
# 1 bar = 1.5 seconds
# So each beat is 0.375 seconds

# Helper function to convert time to seconds
def bar_to_time(bar_number):
    return bar_number * 1.5

# Helper function to convert beat to time
def beat_to_time(beat_number):
    return beat_number * 0.375

# --- Bar 1: Little Ray (Drums) ---
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
# Time: 0.0 to 1.5 seconds

# Kick on beat 1 and 3
kick_notes = [36]  # Kick drum
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat_to_time(beat), end=beat_to_time(beat) + 0.1)
    drum_program.notes.append(note)

# Snare on 2 and 4
snare_notes = [38]  # Snare drum
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat_to_time(beat), end=beat_to_time(beat) + 0.1)
    drum_program.notes.append(note)

# Hi-hat on every eighth note
for beat in range(0, 4):
    for eighth in [0, 0.5]:
        note = pretty_midi.Note(velocity=80, pitch=42, start=beat_to_time(beat) + eighth, end=beat_to_time(beat) + eighth + 0.05)
        drum_program.notes.append(note)

# --- Bar 2: Bass, Piano, Sax come in ---

# Bass (Marcus) - walking line in D minor (D, Eb, F, G, Ab, Bb, C)
# Bar 2: Start on D, walk to Eb, F, G
# Root, b7, b3, 5
# D (2), Eb (3), F (4), G (5)

# Use root and fifth with chromatic approach
# Root on beat 1, fifth on beat 3, chromatic approach on beat 2

# Bar 2, beat 1: D2 (MIDI 38)
note = pretty_midi.Note(velocity=80, pitch=38, start=bar_to_time(1), end=bar_to_time(1) + 0.25)
bass_program.notes.append(note)

# Bar 2, beat 2: C#2 (MIDI 37) - chromatic approach to Eb
note = pretty_midi.Note(velocity=75, pitch=37, start=bar_to_time(1) + 0.375, end=bar_to_time(1) + 0.375 + 0.25)
bass_program.notes.append(note)

# Bar 2, beat 3: G2 (MIDI 43)
note = pretty_midi.Note(velocity=80, pitch=43, start=bar_to_time(1) + 0.75, end=bar_to_time(1) + 0.75 + 0.25)
bass_program.notes.append(note)

# Bar 2, beat 4: Eb2 (MIDI 39)
note = pretty_midi.Note(velocity=75, pitch=39, start=bar_to_time(1) + 1.125, end=bar_to_time(1) + 1.125 + 0.25)
bass_program.notes.append(note)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last

# Bar 2: Dm7 (D, F, Ab, C)
# Open voicing: D (2), F (4), Ab (6), C (7)
# MIDI pitches: D (38), F (41), Ab (44), C (48)

# Play on beat 2 and 4

# Bar 2, beat 2 (1.125s):
note = pretty_midi.Note(velocity=90, pitch=38, start=bar_to_time(1) + 0.375, end=bar_to_time(1) + 0.375 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=41, start=bar_to_time(1) + 0.375, end=bar_to_time(1) + 0.375 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=44, start=bar_to_time(1) + 0.375, end=bar_to_time(1) + 0.375 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=48, start=bar_to_time(1) + 0.375, end=bar_to_time(1) + 0.375 + 0.25)
piano_program.notes.append(note)

# Bar 2, beat 4 (2.25s):
note = pretty_midi.Note(velocity=90, pitch=38, start=bar_to_time(1) + 1.125, end=bar_to_time(1) + 1.125 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=41, start=bar_to_time(1) + 1.125, end=bar_to_time(1) + 1.125 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=44, start=bar_to_time(1) + 1.125, end=bar_to_time(1) + 1.125 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=48, start=bar_to_time(1) + 1.125, end=bar_to_time(1) + 1.125 + 0.25)
piano_program.notes.append(note)

# Sax (You) - Start the melody. One short motif, haunting, incomplete

# Bar 2, beat 1: Tenor sax plays a note that lingers
# D (38) on beat 1, then rests

note = pretty_midi.Note(velocity=110, pitch=38, start=bar_to_time(1), end=bar_to_time(1) + 0.75)
sax_program.notes.append(note)

# Bar 2, beat 3: Another note, then rest

note = pretty_midi.Note(velocity=110, pitch=39, start=bar_to_time(1) + 0.75, end=bar_to_time(1) + 0.75 + 0.5)
sax_program.notes.append(note)

# --- Bar 3: Bass, Piano, Sax continue ---

# Bass: Bar 3 in D minor (walk to F, Ab, Bb)
# F (41), Ab (44), Bb (45), C (48)

# Bar 3, beat 1: F2 (MIDI 41)
note = pretty_midi.Note(velocity=80, pitch=41, start=bar_to_time(2), end=bar_to_time(2) + 0.25)
bass_program.notes.append(note)

# Bar 3, beat 2: Eb2 (MIDI 39) - chromatic approach to F
note = pretty_midi.Note(velocity=75, pitch=39, start=bar_to_time(2) + 0.375, end=bar_to_time(2) + 0.375 + 0.25)
bass_program.notes.append(note)

# Bar 3, beat 3: Bb2 (MIDI 45)
note = pretty_midi.Note(velocity=80, pitch=45, start=bar_to_time(2) + 0.75, end=bar_to_time(2) + 0.75 + 0.25)
bass_program.notes.append(note)

# Bar 3, beat 4: C2 (MIDI 48)
note = pretty_midi.Note(velocity=75, pitch=48, start=bar_to_time(2) + 1.125, end=bar_to_time(2) + 1.125 + 0.25)
bass_program.notes.append(note)

# Piano: Bar 3: Gm7 (G, Bb, D, F)
# Open voicing: G (43), Bb (45), D (47), F (41)

# Bar 3, beat 2 and 4

# Bar 3, beat 2 (1.125s):
note = pretty_midi.Note(velocity=90, pitch=43, start=bar_to_time(2) + 0.375, end=bar_to_time(2) + 0.375 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=45, start=bar_to_time(2) + 0.375, end=bar_to_time(2) + 0.375 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=47, start=bar_to_time(2) + 0.375, end=bar_to_time(2) + 0.375 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=41, start=bar_to_time(2) + 0.375, end=bar_to_time(2) + 0.375 + 0.25)
piano_program.notes.append(note)

# Bar 3, beat 4 (2.25s):
note = pretty_midi.Note(velocity=90, pitch=43, start=bar_to_time(2) + 1.125, end=bar_to_time(2) + 1.125 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=45, start=bar_to_time(2) + 1.125, end=bar_to_time(2) + 1.125 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=47, start=bar_to_time(2) + 1.125, end=bar_to_time(2) + 1.125 + 0.25)
piano_program.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=41, start=bar_to_time(2) + 1.125, end=bar_to_time(2) + 1.125 + 0.25)
piano_program.notes.append(note)

# Sax: Bar 3, beat 1: Rest
# Bar 3, beat 3: Pull back to D (38), incomplete

note = pretty_midi.Note(velocity=110, pitch=38, start=bar_to_time(2) + 0.75, end=bar_to_time(2) + 0.75 + 0.5)
sax_program.notes.append(note)

# --- Bar 4: Sax resolves, hint of something more ---

# Bar 4, beat 1: Tenor sax plays a note that lingers (maybe a Bb or C)
note = pretty_midi.Note(velocity=110, pitch=45, start=bar_to_time(3), end=bar_to_time(3) + 0.75)
sax_program.notes.append(note)

# Bar 4, beat 2: Rest
# Bar 4, beat 3: One more note, hint of resolution
note = pretty_midi.Note(velocity=110, pitch=48, start=bar_to_time(3) + 0.75, end=bar_to_time(3) + 0.75 + 0.5)
sax_program.notes.append(note)

# Save the MIDI file
# midi.write disabled
