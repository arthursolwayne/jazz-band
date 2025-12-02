
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
BPM = 160
time_signature = (4, 4)

# Time per beat in seconds
beat_duration = 60.0 / BPM  # 0.375 seconds per beat
bar_duration = beat_duration * 4  # 1.5 seconds per bar

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM, time_signature=(4, 4))

# Define the key: D Major
D_MAJOR_SCALE = [2, 4, 5, 7, 9, 11, 12]  # D, E, F#, G, A, B, C#

# Define instruments
bass_instrument = Instrument(program=33, is_drum=False, name="Bass")
piano_instrument = Instrument(program=0, is_drum=False, name="Piano")
drum_instrument = Instrument(program=0, is_drum=True, name="Drums")
tenor_sax_instrument = Instrument(program=66, is_drum=False, name="Tenor Sax")

pm.instruments = [bass_instrument, piano_instrument, drum_instrument, tenor_sax_instrument]

#*************************************************
# BAR 1: DRUMS ONLY (Little Ray)
#*************************************************
# Kick on 1 and 3
drum_instrument.notes.append(Note(36, 60, 0.0, 0.375))  # Kick on beat 1
drum_instrument.notes.append(Note(36, 60, 1.125, 0.375))  # Kick on beat 3

# Snare on 2 and 4
drum_instrument.notes.append(Note(38, 60, 0.75, 0.375))  # Snare on beat 2
drum_instrument.notes.append(Note(38, 60, 1.875, 0.375))  # Snare on beat 4

# Hi-hat on every eighth note
for i in range(0, 8):
    drum_instrument.notes.append(Note(42, 60, i * 0.1875, 0.1875))  # 8th notes

#*************************************************
# BAR 2: BASS, PIANO, SAX ENTER
#*************************************************

# Bass line (walking line with chromatic approaches)
# D -> Eb -> F# -> G -> A -> B -> C# -> D
bass_notes = [2, 3, 5, 6, 7, 9, 11, 12]
for i, note in enumerate(bass_notes):
    start = bar_duration + i * beat_duration
    duration = beat_duration / 4  # 16th note
    bass_instrument.notes.append(Note(note + 12, 60, start, duration))

# Piano: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# G7: G, Bb, D, F
piano_notes = [
    # Bar 2: D7 on beat 1
    Note(2, 60, bar_duration, 0.1875),
    Note(4, 60, bar_duration, 0.1875),
    Note(7, 60, bar_duration, 0.1875),
    Note(10, 60, bar_duration, 0.1875),
    
    # Bar 2: G7 on beat 3
    Note(7, 60, bar_duration + 1.125, 0.1875),
    Note(9, 60, bar_duration + 1.125, 0.1875),
    Note(12, 60, bar_duration + 1.125, 0.1875),
    Note(10, 60, bar_duration + 1.125, 0.1875),
]

piano_instrument.notes.extend(piano_notes)

# Tenor Sax: Melody (start of motif)
# D -> F# -> A -> rest (1 bar)
# Then repeat and resolve in next bar
tenor_sax_notes = [
    Note(2, 60, bar_duration, 0.375),  # D
    Note(5, 60, bar_duration + 0.75, 0.375),  # F#
    Note(7, 60, bar_duration + 1.5, 0.375),  # A
]

tenor_sax_instrument.notes.extend(tenor_sax_notes)

#*************************************************
# BAR 3: SAX CONTINUES, PIANO STAYS, BASS WALKS
#*************************************************

# Bass line continues
bass_notes = [12, 11, 9, 7, 6, 5, 4, 3]
for i, note in enumerate(bass_notes):
    start = bar_duration * 2 + i * beat_duration
    duration = beat_duration / 4
    bass_instrument.notes.append(Note(note + 12, 60, start, duration))

# Piano stays on G7
piano_notes = [
    Note(7, 60, bar_duration * 2, 0.1875),
    Note(9, 60, bar_duration * 2, 0.1875),
    Note(12, 60, bar_duration * 2, 0.1875),
    Note(10, 60, bar_duration * 2, 0.1875),
]

piano_instrument.notes.extend(piano_notes)

# Tenor Sax: Continue the motif
# D -> F# -> A -> rest
tenor_sax_notes = [
    Note(2, 60, bar_duration * 2, 0.375),  # D
    Note(5, 60, bar_duration * 2 + 0.75, 0.375),  # F#
    Note(7, 60, bar_duration * 2 + 1.5, 0.375),  # A
]

tenor_sax_instrument.notes.extend(tenor_sax_notes)

#*************************************************
# BAR 4: RESOLUTION, EVERYONE IN
#*************************************************

# Bass line continues
bass_notes = [3, 2, 12, 11, 10, 9, 7, 6]
for i, note in enumerate(bass_notes):
    start = bar_duration * 3 + i * beat_duration
    duration = beat_duration / 4
    bass_instrument.notes.append(Note(note + 12, 60, start, duration))

# Piano: D7 again (resolution)
piano_notes = [
    Note(2, 60, bar_duration * 3, 0.1875),
    Note(4, 60, bar_duration * 3, 0.1875),
    Note(7, 60, bar_duration * 3, 0.1875),
    Note(10, 60, bar_duration * 3, 0.1875),
]

piano_instrument.notes.extend(piano_notes)

# Tenor Sax: Resolve the motif
# D -> F# -> A -> D
tenor_sax_notes = [
    Note(2, 60, bar_duration * 3, 0.375),  # D
    Note(5, 60, bar_duration * 3 + 0.75, 0.375),  # F#
    Note(7, 60, bar_duration * 3 + 1.5, 0.375),  # A
    Note(2, 60, bar_duration * 3 + 2.25, 0.375),  # D
]

tenor_sax_instrument.notes.extend(tenor_sax_notes)

#*************************************************
# Save the MIDI file
#*************************************************
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
