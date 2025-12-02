
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set the key signature to D major (no sharps/flats, but D is the tonic)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0.0)]  # 2 is D major

# Add instruments
bass_program = Program(33, 0)  # Electric Bass
piano_program = Program(0, 0)  # Acoustic Grand Piano
drums_program = Program(128, 0)  # Drums
sax_program = Program(64, 0)    # Tenor Saxophone

bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define the tempo in beats per minute
BPM = 160
beat = 60.0 / BPM  # seconds per beat
bar = 4 * beat  # seconds per bar

# Define note durations in seconds
whole_note = 4 * beat
half_note = 2 * beat
quarter_note = beat
eighth_note = beat / 2
sixteenth_note = beat / 4

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar is 6 seconds, beat = 0.375s, 16 sixteenths per bar

# Kick on 1 and 3 (beats 1 and 3)
drums.notes.append(Note(36, 64, 0.0, 0.1))
drums.notes.append(Note(36, 64, 2.25, 0.1))

# Snare on 2 and 4 (beats 2 and 4)
drums.notes.append(Note(38, 64, 0.75, 0.1))
drums.notes.append(Note(38, 64, 3.0, 0.1))

# Hihat on every eighth (every 0.375s)
for i in range(16):
    time = i * 0.375
    drums.notes.append(Note(42, 64, time, 0.05))

# Bar 2: Everyone enters, sax takes the melody

# Bass: Walking line, chromatic approaches, unique each time
# We'll use a D7 chord: D, F#, A, C#
# Walking bass: D - F# - A - C# - D
# Let's stagger the notes slightly for individuality

bass_notes = [
    Note(62, 64, 0.0, 0.375),   # D
    Note(67, 64, 0.75, 0.375),  # F#
    Note(69, 64, 1.5, 0.375),   # A
    Note(71, 64, 2.25, 0.375),  # C#
    Note(62, 64, 3.0, 0.375)    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# D7 (D, F#, A, C#) with 7th chords: D7, A7, D7, G7 (on 2 and 4)
# Each chord lasts 0.5 seconds, played on 2 and 4

# Bar 2, beat 2: D7
piano.notes.append(Note(62, 80, 0.75, 0.5))
piano.notes.append(Note(67, 80, 0.75, 0.5))
piano.notes.append(Note(69, 80, 0.75, 0.5))
piano.notes.append(Note(71, 80, 0.75, 0.5))

# Bar 2, beat 4: G7
piano.notes.append(Note(67, 80, 3.0, 0.5))
piano.notes.append(Note(72, 80, 3.0, 0.5))
piano.notes.append(Note(74, 80, 3.0, 0.5))
piano.notes.append(Note(76, 80, 3.0, 0.5))

# Sax: Tenor sax — your moment. Short motif, hang, come back.

# Motif: D, F#, A, rest — then return on the next bar (bar 3)
# D (62) on beat 1
sax.notes.append(Note(62, 96, 0.0, 0.25))
# F# (67) on beat 2
sax.notes.append(Note(67, 96, 0.75, 0.25))
# A (69) on beat 3
sax.notes.append(Note(69, 96, 1.5, 0.25))
# Rest on beat 4
# No note here — silence speaks

# Bar 3: Piano fills, bass continues, drums keep going
# Sax returns and finishes the motif on beat 1 (bar 3)

# Sax: D (62) on beat 1 of bar 3 (time = 3.0)
sax.notes.append(Note(62, 96, 3.0, 0.25))
# C# (71) on beat 2 of bar 3 (time = 3.75)
sax.notes.append(Note(71, 96, 3.75, 0.25))
# B (71) on beat 3 of bar 3 (time = 4.5)
sax.notes.append(Note(71, 96, 4.5, 0.25))
# D (62) on beat 4 of bar 3 (time = 5.25)
sax.notes.append(Note(62, 96, 5.25, 0.25))

# Bar 4: Everyone resolves. Piano plays final D7, bass walks to D, sax ends on D.

# Piano: D7 on beat 4
piano.notes.append(Note(62, 80, 5.25, 0.5))
piano.notes.append(Note(67, 80, 5.25, 0.5))
piano.notes.append(Note(69, 80, 5.25, 0.5))
piano.notes.append(Note(71, 80, 5.25, 0.5))

# Bass: D again, hanging on bar 4
bass.notes.append(Note(62, 64, 5.25, 0.75))

# Write the MIDI file to disk
pm.write("jazz_intro.mid")
