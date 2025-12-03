
import pretty_midi
from pretty_midi import Note, Instrument
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Initialize the PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll use Fm7 (F, Ab, Bb, Db) for the root chord
# Let's choose a key of F minor for this session

# Define the note_to_midi function
def note_to_midi(note, octave):
    return pretty_midi.note_number_from_name(note + str(octave))

# Define instruments
# 1. Drum Kit (Little Ray)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Using piano for simplicity, but can map to drums later
drum_instrument = Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drum_instrument)

# 2. Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
bass_instrument = Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# 3. Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# 4. Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_instrument = Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Define time in seconds for each bar
bar_length = 6.0 / 4  # 6 seconds for 4 bars, so 1.5 seconds per bar

# Define the timing in seconds
bar_1_start = 0.0
bar_2_start = 1.5
bar_3_start = 3.0
bar_4_start = 4.5

# -- DRUMS (Little Ray) --
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
def add_drum_notes(instrument, start_time, duration, pattern):
    for i, note in enumerate(pattern):
        if note:
            note_time = start_time + (i * duration / 8)
            note_obj = Note(velocity=100, start=note_time, end=note_time + 0.05)
            instrument.notes.append(note_obj)

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_pattern_bar1 = [1,0,1,0,1,0,1,0]  # Kick
drum_pattern_bar1_snare = [0,1,0,1,0,1,0,1]  # Snare
drum_pattern_bar1_hihat = [1]*8  # Hihat on every 8th
add_drum_notes(drum_instrument, bar_1_start, bar_length, drum_pattern_bar1)
add_drum_notes(drum_instrument, bar_1_start, bar_length, drum_pattern_bar1_snare)
add_drum_notes(drum_instrument, bar_1_start, bar_length, drum_pattern_bar1_hihat)

# Bar 2: Same pattern
add_drum_notes(drum_instrument, bar_2_start, bar_length, drum_pattern_bar1)
add_drum_notes(drum_instrument, bar_2_start, bar_length, drum_pattern_bar1_snare)
add_drum_notes(drum_instrument, bar_2_start, bar_length, drum_pattern_bar1_hihat)

# Bar 3: Same
add_drum_notes(drum_instrument, bar_3_start, bar_length, drum_pattern_bar1)
add_drum_notes(drum_instrument, bar_3_start, bar_length, drum_pattern_bar1_snare)
add_drum_notes(drum_instrument, bar_3_start, bar_length, drum_pattern_bar1_hihat)

# Bar 4: Same
add_drum_notes(drum_instrument, bar_4_start, bar_length, drum_pattern_bar1)
add_drum_notes(drum_instrument, bar_4_start, bar_length, drum_pattern_bar1_snare)
add_drum_notes(drum_instrument, bar_4_start, bar_length, drum_pattern_bar1_hihat)

# -- BASS (Marcus) --
# Walking line: D2-G2 (MIDI 38 to 43)
# Root and fifth with chromatic approaches
# Fm7: F (53), Ab (56), Bb (58), Db (60)

# Bar 1: F (root) and chromatic approach
note_f = Note(velocity=100, start=bar_1_start, end=bar_1_start + 0.5)
note_f_b = Note(velocity=90, start=bar_1_start + 0.25, end=bar_1_start + 0.5)
bass_instrument.notes.append(note_f)
bass_instrument.notes.append(note_f_b)

# Bar 2: Gb (fifth) and Ab (chromatic approach)
note_gb = Note(velocity=100, start=bar_2_start, end=bar_2_start + 0.5)
note_ab = Note(velocity=90, start=bar_2_start + 0.25, end=bar_2_start + 0.5)
bass_instrument.notes.append(note_gb)
bass_instrument.notes.append(note_ab)

# Bar 3: Bb (chromatic) and Ab (root)
note_bb = Note(velocity=100, start=bar_3_start, end=bar_3_start + 0.5)
note_ab_root = Note(velocity=90, start=bar_3_start + 0.25, end=bar_3_start + 0.5)
bass_instrument.notes.append(note_bb)
bass_instrument.notes.append(note_ab_root)

# Bar 4: Db (chromatic) and F (root again)
note_db = Note(velocity=100, start=bar_4_start, end=bar_4_start + 0.5)
note_f_root = Note(velocity=90, start=bar_4_start + 0.25, end=bar_4_start + 0.5)
bass_instrument.notes.append(note_db)
bass_instrument.notes.append(note_f_root)

# -- PIANO (Diane) --
# Open voicings, different chord each bar, comp on 2 and 4
# Fm7 (F, Ab, Bb, Db)
# Gbm7 (Gb, Bb, Db, F)
# Bbmaj7 (Bb, Db, F, Ab)
# Dbmaj7 (Db, F, Ab, Bb)

def add_piano_notes(instrument, start_time, notes, duration=0.5):
    for note in notes:
        n = Note(velocity=110, start=start_time, end=start_time + duration)
        n.pitch = note
        instrument.notes.append(n)

# Bar 1: Fm7 (F, Ab, Bb, Db)
add_piano_notes(piano_instrument, bar_1_start, [53, 56, 58, 60])

# Bar 2: Gbm7 (Gb, Bb, Db, F)
add_piano_notes(piano_instrument, bar_2_start, [57, 58, 60, 53])

# Bar 3: Bbmaj7 (Bb, Db, F, Ab)
add_piano_notes(piano_instrument, bar_3_start, [58, 60, 53, 56])

# Bar 4: Dbmaj7 (Db, F, Ab, Bb)
add_piano_notes(piano_instrument, bar_4_start, [60, 53, 56, 58])

# -- SAX (You) --
# One short motif, start it, leave it hanging, come back and finish it
# Fm7: F (53), Ab (56), Bb (58), Db (60)
# Motif: F - Ab - rest - Bb
# Let it hang on 3rd beat, come back on 4th beat with Db

# Bar 1: F (53)
note_f_motif = Note(velocity=110, start=bar_1_start, end=bar_1_start + 0.25)
sax_instrument.notes.append(note_f_motif)

# Bar 1: Ab (56)
note_ab = Note(velocity=110, start=bar_1_start + 0.25, end=bar_1_start + 0.5)
sax_instrument.notes.append(note_ab)

# Bar 2: Rest

# Bar 3: Rest

# Bar 4: Bb (58)
note_bb = Note(velocity=110, start=bar_4_start, end=bar_4_start + 0.25)
sax_instrument.notes.append(note_bb)

# Bar 4: Db (60)
note_db = Note(velocity=110, start=bar_4_start + 0.25, end=bar_4_start + 0.5)
sax_instrument.notes.append(note_db)

# Save the MIDI file
pm.write("dante_russo_intro.mid")

print("MIDI file written as 'dante_russo_intro.mid'")
