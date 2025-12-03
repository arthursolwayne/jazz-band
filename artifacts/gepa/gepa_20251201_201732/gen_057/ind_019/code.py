
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define the key: F minor (F, Gb, Ab, Bb, Bb, Db, Eb)
# Use F as the tonic, and build from there.

# Constants
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT  # 4 beats per bar
NOTE_DURATION = 0.5  # Half note
EIGHTH_NOTE = NOTE_DURATION / 2
QUARTER_NOTE = NOTE_DURATION
HALF_NOTE = NOTE_DURATION * 2
ONE_EIGHTH = BEAT / 2
ONE_QUARTER = BEAT
ONE_HALF = BEAT * 2

# Functions to create notes
def create_note(pitch, start, end, velocity):
    return Note(pitch=pitch, start=start, end=end, velocity=velocity)

def create_rest(start, end):
    return Note(pitch=-1, start=start, end=end, velocity=0)

def add_notes_to_instrument(instrument, notes):
    for note in notes:
        instrument.notes.append(note)

# Create instruments
# Drums (Little Ray)
drum_program = Program(program=0)
drum_instrument = Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# Bass (Marcus)
bass_program = Program(program=33)  # Electric Bass
bass_instrument = Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# Piano (Diane)
piano_program = Program(program=0)  # Acoustic Grand Piano
piano_instrument = Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# Tenor Sax (You)
sax_program = Program(program=65)  # Alto Saxophone (close enough for tenor)
sax_instrument = Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Bar 1: Little Ray alone - tight, driving, slightly off-kilter
bar_1_start = 0.0
bar_1_end = BAR_DURATION

# Kick on 1 and 3
drum_kick_1 = create_note(pretty_midi.note_number_from_name('C1'), bar_1_start, bar_1_start + ONE_QUARTER, 100)
drum_kick_3 = create_note(pretty_midi.note_number_from_name('C1'), bar_1_start + ONE_HALF, bar_1_start + ONE_HALF + ONE_QUARTER, 100)

# Snare on 2 and 4
drum_snare_2 = create_note(pretty_midi.note_number_from_name('Snare'), bar_1_start + ONE_QUARTER, bar_1_start + ONE_QUARTER + ONE_EIGHTH, 110)
drum_snare_4 = create_note(pretty_midi.note_number_from_name('Snare'), bar_1_start + ONE_HALF * 2, bar_1_start + ONE_HALF * 2 + ONE_EIGHTH, 110)

# Hihat on every eighth
hihat_notes = [
    create_note(pretty_midi.note_number_from_name('C#1'), bar_1_start + i * ONE_EIGHTH, bar_1_start + i * ONE_EIGHTH + ONE_EIGHTH / 2, 80)
    for i in range(8)
]

# Add to drum instrument
add_notes_to_instrument(drum_instrument, [drum_kick_1, drum_kick_3, drum_snare_2, drum_snare_4] + hihat_notes)

# Bar 2: Bass enters with walking line (roots and fifths with chromatic approaches)
bar_2_start = bar_1_end

# Fm7: F, Ab, C, Eb (or Ab, C, Eb, F depending on voicing)
# Walking line: Ab (root), Bb (chromatic approach), C (fifth), Eb (root), F (chromatic), Gb (fifth), Ab (root), Bb (chromatic), C (fifth), Eb (root)... etc.

# Bass line in Fm, walking with chromatic approaches
bass_notes = [
    create_note(pretty_midi.note_number_from_name('Ab2'), bar_2_start, bar_2_start + ONE_QUARTER, 70),  # Chromatic approach
    create_note(pretty_midi.note_number_from_name('C2'), bar_2_start + ONE_QUARTER, bar_2_start + ONE_HALF, 70),  # Fifth
    create_note(pretty_midi.note_number_from_name('Eb2'), bar_2_start + ONE_HALF, bar_2_start + ONE_HALF + ONE_QUARTER, 70),  # Root
    create_note(pretty_midi.note_number_from_name('F2'), bar_2_start + ONE_HALF + ONE_QUARTER, bar_2_start + ONE_HALF * 2, 70),  # Chromatic approach
]

add_notes_to_instrument(bass_instrument, bass_notes)

# Bar 2: Piano enters with open voicing
# Diane plays a dark, unresolved chord — F7 with a #11 (Ab) and a diminished Bb
# F7(#11) = F, Ab, C, E, Bb (diminished)

# Open voicings, different chord each bar, resolve on last bar
# Bar 2: F7(#11)
piano_notes_bar2 = [
    create_note(pretty_midi.note_number_from_name('F3'), bar_2_start, bar_2_start + ONE_HALF, 100),
    create_note(pretty_midi.note_number_from_name('Ab3'), bar_2_start, bar_2_start + ONE_HALF, 90),
    create_note(pretty_midi.note_number_from_name('C3'), bar_2_start, bar_2_start + ONE_HALF, 80),
    create_note(pretty_midi.note_number_from_name('E3'), bar_2_start, bar_2_start + ONE_HALF, 70),
    create_note(pretty_midi.note_number_from_name('Bb3'), bar_2_start, bar_2_start + ONE_HALF, 60),
]

add_notes_to_instrument(piano_instrument, piano_notes_bar2)

# Bar 3: Full band, sax melody starts — haunting, incomplete, with rests

bar_3_start = bar_2_end

# Tenor sax melody — minimal, with rests, haunting, incomplete
# Motif: F (start), then a descending tritone (C to F), then a rest, then a return
# Use dynamic contrast, let the silence speak

sax_notes_bar3 = [
    create_note(pretty_midi.note_number_from_name('F4'), bar_3_start, bar_3_start + ONE_EIGHTH, 110),
    create_note(pretty_midi.note_number_from_name('C4'), bar_3_start + ONE_EIGHTH, bar_3_start + ONE_QUARTER, 80),
    create_rest(bar_3_start + ONE_QUARTER, bar_3_start + ONE_HALF),
    create_note(pretty_midi.note_number_from_name('F4'), bar_3_start + ONE_HALF, bar_3_start + ONE_HALF + ONE_EIGHTH, 110),
]

add_notes_to_instrument(sax_instrument, sax_notes_bar3)

# Bar 4: Piano and bass resolve, sax melody ends with a question
bar_4_start = bar_3_end

# Bass: C (fifth of Fm), resolve slightly
bass_notes_bar4 = [
    create_note(pretty_midi.note_number_from_name('C2'), bar_4_start, bar_4_start + ONE_QUARTER, 70),
]

add_notes_to_instrument(bass_instrument, bass_notes_bar4)

# Piano: Fm7 with a Bb (diminished) — unresolved, lingering
piano_notes_bar4 = [
    create_note(pretty_midi.note_number_from_name('F3'), bar_4_start, bar_4_start + ONE_HALF, 100),
    create_note(pretty_midi.note_number_from_name('Ab3'), bar_4_start, bar_4_start + ONE_HALF, 90),
    create_note(pretty_midi.note_number_from_name('C3'), bar_4_start, bar_4_start + ONE_HALF, 80),
    create_note(pretty_midi.note_number_from_name('Eb3'), bar_4_start, bar_4_start + ONE_HALF, 70),
    create_note(pretty_midi.note_number_from_name('Bb3'), bar_4_start, bar_4_start + ONE_HALF, 60),
]

add_notes_to_instrument(piano_instrument, piano_notes_bar4)

# Drums continue with same pattern
bar_4_end = bar_4_start + BAR_DURATION

# Kick on 1 and 3
drum_kick_1_bar4 = create_note(pretty_midi.note_number_from_name('C1'), bar_4_start, bar_4_start + ONE_QUARTER, 100)
drum_kick_3_bar4 = create_note(pretty_midi.note_number_from_name('C1'), bar_4_start + ONE_HALF, bar_4_start + ONE_HALF + ONE_QUARTER, 100)

# Snare on 2 and 4
drum_snare_2_bar4 = create_note(pretty_midi.note_number_from_name('Snare'), bar_4_start + ONE_QUARTER, bar_4_start + ONE_QUARTER + ONE_EIGHTH, 110)
drum_snare_4_bar4 = create_note(pretty_midi.note_number_from_name('Snare'), bar_4_start + ONE_HALF * 2, bar_4_start + ONE_HALF * 2 + ONE_EIGHTH, 110)

# Hihat on every eighth
hihat_notes_bar4 = [
    create_note(pretty_midi.note_number_from_name('C#1'), bar_4_start + i * ONE_EIGHTH, bar_4_start + i * ONE_EIGHTH + ONE_EIGHTH / 2, 80)
    for i in range(8)
]

add_notes_to_instrument(drum_instrument, [drum_kick_1_bar4, drum_kick_3_bar4, drum_snare_2_bar4, drum_snare_4_bar4] + hihat_notes_bar4)

# Save the MIDI file
pm.write("jazz_intro_fm.mid")
