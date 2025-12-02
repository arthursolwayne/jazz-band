
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create an instrument for the tenor sax (program 64 for soprano sax, similar enough for this context)
sax_program = pretty_midi.instrument_name_to_program('Soprano Saxophone')
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# Create an instrument for the piano
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

# Create an instrument for the bass
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

# Create an instrument for the drums
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

# Time per bar at 160 BPM in seconds
BAR_DURATION = 6.0 / 4  # 1.5 seconds per bar
BEAT_DURATION = BAR_DURATION / 4  # 0.375 seconds per beat
NOTE_DURATION = BEAT_DURATION / 4  # 0.09375 seconds per eighth note

# Function to create a note
def note(note_number, start, duration, velocity=100):
    return pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=start + duration)

# Function to create a drum hit
def drum(note_number, start, duration=0.05):
    return note(note_number, start, duration, velocity=100)

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_1_start = 0.0

# Kick on 1
drums.notes.append(drum(36, bar_1_start))  # Kick
# Snare on 2
drums.notes.append(drum(38, bar_1_start + BEAT_DURATION))  # Snare
# Kick on 3
drums.notes.append(drum(36, bar_1_start + 2 * BEAT_DURATION))  # Kick
# Snare on 4
drums.notes.append(drum(38, bar_1_start + 3 * BEAT_DURATION))  # Snare
# Hi-hat on every eighth
for i in range(8):
    drums.notes.append(drum(42, bar_1_start + i * NOTE_DURATION))  # Hi-hat

# Bar 2: Everyone comes in

# Bass line - Marcus (walking line, chromatic approaches)
bass_notes = [
    note(45, bar_1_start + BAR_DURATION, NOTE_DURATION, 60),  # F
    note(46, bar_1_start + BAR_DURATION + NOTE_DURATION, NOTE_DURATION, 60),  # F#
    note(47, bar_1_start + BAR_DURATION + 2 * NOTE_DURATION, NOTE_DURATION, 60),  # G
    note(49, bar_1_start + BAR_DURATION + 3 * NOTE_DURATION, NOTE_DURATION, 60),  # A
    note(50, bar_1_start + BAR_DURATION + 4 * NOTE_DURATION, NOTE_DURATION, 60),  # A#
    note(51, bar_1_start + BAR_DURATION + 5 * NOTE_DURATION, NOTE_DURATION, 60),  # B
    note(53, bar_1_start + BAR_DURATION + 6 * NOTE_DURATION, NOTE_DURATION, 60),  # C
    note(55, bar_1_start + BAR_DURATION + 7 * NOTE_DURATION, NOTE_DURATION, 60),  # D
]
bass.notes.extend(bass_notes)

# Piano - Diane (7th chords, comp on 2 and 4)
piano_notes = [
    note(64, bar_1_start + BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),  # C7
    note(69, bar_1_start + BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(71, bar_1_start + BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(74, bar_1_start + BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(64, bar_1_start + BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),  # C7
    note(69, bar_1_start + BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
    note(71, bar_1_start + BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
    note(74, bar_1_start + BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
]
piano.notes.extend(piano_notes)

# Tenor sax - Dante (the melody)
# Start with a whisper, then build into a cry

# Note 1: F (45) - whisper, short, soft
sax.notes.append(note(45, bar_1_start + BAR_DURATION, 0.05, 60))
# Note 2: Bb (48) - slightly louder, longer
sax.notes.append(note(48, bar_1_start + BAR_DURATION + 0.05, 0.1, 70))
# Note 3: C (52) - louder, more expressive
sax.notes.append(note(52, bar_1_start + BAR_DURATION + 0.15, 0.15, 85))
# Note 4: F (45) - cry, long, lingering
sax.notes.append(note(45, bar_1_start + BAR_DURATION + 0.3, 0.3, 100))

# Bar 3: Continue the story

# Bass continues the walking line
bass_notes = [
    note(56, bar_1_start + 2 * BAR_DURATION, NOTE_DURATION, 60),  # D
    note(57, bar_1_start + 2 * BAR_DURATION + NOTE_DURATION, NOTE_DURATION, 60),  # D#
    note(58, bar_1_start + 2 * BAR_DURATION + 2 * NOTE_DURATION, NOTE_DURATION, 60),  # E
    note(60, bar_1_start + 2 * BAR_DURATION + 3 * NOTE_DURATION, NOTE_DURATION, 60),  # F
    note(61, bar_1_start + 2 * BAR_DURATION + 4 * NOTE_DURATION, NOTE_DURATION, 60),  # F#
    note(62, bar_1_start + 2 * BAR_DURATION + 5 * NOTE_DURATION, NOTE_DURATION, 60),  # G
    note(64, bar_1_start + 2 * BAR_DURATION + 6 * NOTE_DURATION, NOTE_DURATION, 60),  # A
    note(65, bar_1_start + 2 * BAR_DURATION + 7 * NOTE_DURATION, NOTE_DURATION, 60),  # A#
]
bass.notes.extend(bass_notes)

# Piano continues comping
piano_notes = [
    note(67, bar_1_start + 2 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),  # D7
    note(72, bar_1_start + 2 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(74, bar_1_start + 2 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(77, bar_1_start + 2 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(67, bar_1_start + 2 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),  # D7
    note(72, bar_1_start + 2 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
    note(74, bar_1_start + 2 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
    note(77, bar_1_start + 2 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
]
piano.notes.extend(piano_notes)

# Tenor sax continues the melody (builds naturally)
# Note 1: A (57) - soft, but with tension
sax.notes.append(note(57, bar_1_start + 2 * BAR_DURATION, 0.05, 60))
# Note 2: D (62) - more tension
sax.notes.append(note(62, bar_1_start + 2 * BAR_DURATION + 0.05, 0.1, 70))
# Note 3: F (45) - resolution, but not quite
sax.notes.append(note(45, bar_1_start + 2 * BAR_DURATION + 0.15, 0.15, 85))
# Note 4: A (57) - lingering, unresolved
sax.notes.append(note(57, bar_1_start + 2 * BAR_DURATION + 0.3, 0.3, 100))

# Bar 4: Final bar, saxophone returns to the motif, but with a twist

# Bass continues the walking line
bass_notes = [
    note(66, bar_1_start + 3 * BAR_DURATION, NOTE_DURATION, 60),  # Bb
    note(67, bar_1_start + 3 * BAR_DURATION + NOTE_DURATION, NOTE_DURATION, 60),  # B
    note(69, bar_1_start + 3 * BAR_DURATION + 2 * NOTE_DURATION, NOTE_DURATION, 60),  # C
    note(71, bar_1_start + 3 * BAR_DURATION + 3 * NOTE_DURATION, NOTE_DURATION, 60),  # D
    note(72, bar_1_start + 3 * BAR_DURATION + 4 * NOTE_DURATION, NOTE_DURATION, 60),  # D#
    note(74, bar_1_start + 3 * BAR_DURATION + 5 * NOTE_DURATION, NOTE_DURATION, 60),  # E
    note(76, bar_1_start + 3 * BAR_DURATION + 6 * NOTE_DURATION, NOTE_DURATION, 60),  # F
    note(78, bar_1_start + 3 * BAR_DURATION + 7 * NOTE_DURATION, NOTE_DURATION, 60),  # F#
]
bass.notes.extend(bass_notes)

# Piano continues comping
piano_notes = [
    note(69, bar_1_start + 3 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),  # F7
    note(74, bar_1_start + 3 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(76, bar_1_start + 3 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(79, bar_1_start + 3 * BAR_DURATION + 2 * BEAT_DURATION, NOTE_DURATION, 80),
    note(69, bar_1_start + 3 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),  # F7
    note(74, bar_1_start + 3 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
    note(76, bar_1_start + 3 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
    note(79, bar_1_start + 3 * BAR_DURATION + 4 * BEAT_DURATION, NOTE_DURATION, 80),
]
piano.notes.extend(piano_notes)

# Tenor sax: Return to the original motif, but with a twist — end on a Bb
# Note 1: F (45) - whisper again
sax.notes.append(note(45, bar_1_start + 3 * BAR_DURATION, 0.05, 60))
# Note 2: Bb (48) - slightly louder, but with a question
sax.notes.append(note(48, bar_1_start + 3 * BAR_DURATION + 0.05, 0.1, 70))
# Note 3: C (52) - more intense
sax.notes.append(note(52, bar_1_start + 3 * BAR_DURATION + 0.15, 0.15, 85))
# Note 4: Bb (48) - end on a question — but let the silence speak
sax.notes.append(note(48, bar_1_start + 3 * BAR_DURATION + 0.3, 0.3, 100))

# Write the MIDI file
pm.write("dante_intro.mid")
print("MIDI file generated: 'dante_intro.mid'")
