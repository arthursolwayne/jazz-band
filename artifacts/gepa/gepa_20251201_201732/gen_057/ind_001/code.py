
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
bass_program = Program(33)  # Acoustic Bass
piano_program = Program(0)  # Acoustic Grand Piano
drums_program = Program(0)  # Acoustic Grand Piano (for MIDI drum kit)
sax_program = Program(64)   # Tenor Saxophone

# Create instruments
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program, is_drum=True)
sax = Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [bass, piano, drums, sax]

# Define tempo (BPM = 160) => beat duration = 0.375s
beat_duration = 0.375
bar_duration = 4 * beat_duration  # 1.5 seconds per bar
total_duration = 4 * bar_duration  # 6 seconds total

# --- BASS LINE (Marcus) ---
# Root and fifth with chromatic approaches, walking line in Fm7 (F, C, Ab, D)
# Root motion: F -> Bb -> Ab -> D -> F

# Bar 1 (0 - 1.5s): F, C, Ab, D
# Bar 2 (1.5 - 3s): Bb, F, D, Ab
# Bar 3 (3 - 4.5s): Ab, D, F, Bb
# Bar 4 (4.5 - 6s): D, F, Bb, Ab

# Bass notes in MIDI numbers: F2=53, C2=60, Ab2=56, D2=62, Bb2=57

# Bar 1
bass.notes.append(Note(60, 0.0, 53, 0.375))  # C -> F
bass.notes.append(Note(53, 0.375, 56, 0.375))  # F -> Ab
bass.notes.append(Note(56, 0.75, 62, 0.375))  # Ab -> D
bass.notes.append(Note(62, 1.125, 53, 0.375))  # D -> F

# Bar 2
bass.notes.append(Note(53, 1.5, 57, 0.375))  # F -> Bb
bass.notes.append(Note(57, 1.875, 60, 0.375))  # Bb -> F
bass.notes.append(Note(60, 2.25, 62, 0.375))  # F -> D
bass.notes.append(Note(62, 2.625, 56, 0.375))  # D -> Ab

# Bar 3
bass.notes.append(Note(56, 3.0, 62, 0.375))  # Ab -> D
bass.notes.append(Note(62, 3.375, 53, 0.375))  # D -> F
bass.notes.append(Note(53, 3.75, 57, 0.375))  # F -> Bb
bass.notes.append(Note(57, 4.125, 60, 0.375))  # Bb -> F

# Bar 4
bass.notes.append(Note(60, 4.5, 62, 0.375))  # F -> D
bass.notes.append(Note(62, 4.875, 53, 0.375))  # D -> F
bass.notes.append(Note(53, 5.25, 57, 0.375))  # F -> Bb
bass.notes.append(Note(57, 5.625, 56, 0.375))  # Bb -> Ab

# --- PIANO (Diane) ---
# Open voicings, different chord each bar, resolve on the last bar
# Bar 1: Fm7 (F, Ab, C, D) -> open voicing
# Bar 2: Bbm7 (Bb, Db, F, G) -> open voicing
# Bar 3: Ab7 (Ab, C, Eb, Gb) -> open voicing
# Bar 4: D7 (D, F#, A, C) -> resolves to Fm7

# Bar 1: Fm7
# F (53), Ab (56), C (60), D (62)
# Chord at beat 2
piano.notes.append(Note(53, 1.5, 100, 0.1))
piano.notes.append(Note(56, 1.5, 100, 0.1))
piano.notes.append(Note(60, 1.5, 100, 0.1))
piano.notes.append(Note(62, 1.5, 100, 0.1))

# Bar 2: Bbm7
# Bb (57), Db (59), F (60), G (67)
# Chord at beat 3
piano.notes.append(Note(57, 3.0, 100, 0.1))
piano.notes.append(Note(59, 3.0, 100, 0.1))
piano.notes.append(Note(60, 3.0, 100, 0.1))
piano.notes.append(Note(67, 3.0, 100, 0.1))

# Bar 3: Ab7 (Ab, C, Eb, Gb)
# Ab (56), C (60), Eb (62), Gb (64)
# Chord at beat 1
piano.notes.append(Note(56, 4.5, 100, 0.1))
piano.notes.append(Note(60, 4.5, 100, 0.1))
piano.notes.append(Note(62, 4.5, 100, 0.1))
piano.notes.append(Note(64, 4.5, 100, 0.1))

# Bar 4: D7 (D, F#, A, C)
# D (62), F# (64), A (69), C (60)
# Chord at beat 4
piano.notes.append(Note(62, 5.625, 100, 0.1))
piano.notes.append(Note(64, 5.625, 100, 0.1))
piano.notes.append(Note(69, 5.625, 100, 0.1))
piano.notes.append(Note(60, 5.625, 100, 0.1))

# --- DRUMS (Little Ray) ---
# Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
# Bar 1
drums.notes.append(Note(35, 0.0, 100, 0.1))  # Kick on 1
drums.notes.append(Note(38, 0.375, 100, 0.1))  # Snare on 2
drums.notes.append(Note(42, 0.0, 100, 0.25))  # Hihat on 1 & 2
drums.notes.append(Note(42, 0.375, 100, 0.25))

drums.notes.append(Note(35, 0.75, 100, 0.1))  # Kick on 3
drums.notes.append(Note(38, 1.125, 100, 0.1))  # Snare on 4
drums.notes.append(Note(42, 0.75, 100, 0.25))  # Hihat on 3 & 4
drums.notes.append(Note(42, 1.125, 100, 0.25))

# Bar 2
drums.notes.append(Note(35, 1.5, 100, 0.1))  # Kick on 1
drums.notes.append(Note(38, 1.875, 100, 0.1))  # Snare on 2
drums.notes.append(Note(42, 1.5, 100, 0.25))  # Hihat
drums.notes.append(Note(42, 1.875, 100, 0.25))

drums.notes.append(Note(35, 2.25, 100, 0.1))  # Kick on 3
drums.notes.append(Note(38, 2.625, 100, 0.1))  # Snare on 4
drums.notes.append(Note(42, 2.25, 100, 0.25))  # Hihat
drums.notes.append(Note(42, 2.625, 100, 0.25))

# Bar 3
drums.notes.append(Note(35, 3.0, 100, 0.1))  # Kick on 1
drums.notes.append(Note(38, 3.375, 100, 0.1))  # Snare on 2
drums.notes.append(Note(42, 3.0, 100, 0.25))  # Hihat
drums.notes.append(Note(42, 3.375, 100, 0.25))

drums.notes.append(Note(35, 3.75, 100, 0.1))  # Kick on 3
drums.notes.append(Note(38, 4.125, 100, 0.1))  # Snare on 4
drums.notes.append(Note(42, 3.75, 100, 0.25))  # Hihat
drums.notes.append(Note(42, 4.125, 100, 0.25))

# Bar 4
drums.notes.append(Note(35, 4.5, 100, 0.1))  # Kick on 1
drums.notes.append(Note(38, 4.875, 100, 0.1))  # Snare on 2
drums.notes.append(Note(42, 4.5, 100, 0.25))  # Hihat
drums.notes.append(Note(42, 4.875, 100, 0.25))

drums.notes.append(Note(35, 5.25, 100, 0.1))  # Kick on 3
drums.notes.append(Note(38, 5.625, 100, 0.1))  # Snare on 4
drums.notes.append(Note(42, 5.25, 100, 0.25))  # Hihat
drums.notes.append(Note(42, 5.625, 100, 0.25))

# --- SAX (You) ---
# One short motif, haunting, incomplete
# Start on F (53), then Bb (57), then F again (53), but leave it hanging
# Use small dynamic variations, rests, and space

# Bar 1: Start with a rest
# Bar 2: Play Bb
# Bar 3: Play F again
# Bar 4: Leave it hanging — no note

# Rest in Bar 1
# Bar 2: Bb at beat 2
sax.notes.append(Note(57, 1.5, 90, 0.25))

# Bar 3: F again at beat 3
sax.notes.append(Note(53, 3.0, 80, 0.25))

# Bar 4: No note — leave it hanging

# Save the MIDI file
pm.write("jazz_intro_fminor.mid")
print("MIDI file generated: jazz_intro_fminor.mid")
