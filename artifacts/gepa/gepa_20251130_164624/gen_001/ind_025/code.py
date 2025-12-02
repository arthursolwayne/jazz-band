
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax_instrument = Instrument(program=64, is_drum=False, name='Tenor Saxophone')
bass_instrument = Instrument(program=33, is_drum=False, name='Double Bass')
piano_instrument = Instrument(program=0, is_drum=False, name='Piano')
drum_instrument = Instrument(program=0, is_drum=True, name='Drums')

# Function to add a note
def add_note(instrument, pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    instrument.notes.append(note)

# Time in seconds per beat
beat = 0.375  # 160 BPM = 60 / 160 = 0.375s per beat
bar = beat * 4  # 1.5s per bar

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Only hihat
for i in range(0, 8):
    add_note(drum_instrument, 42, i * beat, i * beat + 0.125, 100)  # hihat on every eighth

# Bar 2: Kick, snare, hihat
for i in range(0, 8):
    add_note(drum_instrument, 36, i * beat + 0.0, i * beat + 0.125, 100)  # kick on 1 and 3
    add_note(drum_instrument, 38, i * beat + 0.5, i * beat + 0.625, 100)  # snare on 2 and 4
    add_note(drum_instrument, 42, i * beat, i * beat + 0.125, 100)  # hihat on every eighth

# Bar 3: Kick, snare, hihat
for i in range(0, 8):
    add_note(drum_instrument, 36, i * beat + 0.0, i * beat + 0.125, 100)  # kick on 1 and 3
    add_note(drum_instrument, 38, i * beat + 0.5, i * beat + 0.625, 100)  # snare on 2 and 4
    add_note(drum_instrument, 42, i * beat, i * beat + 0.125, 100)  # hihat on every eighth

# Bar 4: Kick, snare, hihat
for i in range(0, 8):
    add_note(drum_instrument, 36, i * beat + 0.0, i * beat + 0.125, 100)  # kick on 1 and 3
    add_note(drum_instrument, 38, i * beat + 0.5, i * beat + 0.625, 100)  # snare on 2 and 4
    add_note(drum_instrument, 42, i * beat, i * beat + 0.125, 100)  # hihat on every eighth

# Chromatic walking bass line in D (no repeated notes)
bass_line = [
    65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
    86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
    106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,
    123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
    140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156,
    157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173,
    174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190,
    191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
    208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224,
    225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241,
    242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258,
]

# Bar 1: No bass
# Bar 2-4: Walking bass
for i in range(0, 12):
    add_note(bass_instrument, bass_line[i], i * beat, i * beat + beat, 70)

# Piano comp: 7th chords on beats 2 and 4
# D7 chord: D, F#, A, C
# Bar 2: beat 2 (0.5s)
add_note(piano_instrument, 62, 0.5, 0.5 + 0.25, 100)
add_note(piano_instrument, 67, 0.5, 0.5 + 0.25, 100)
add_note(piano_instrument, 74, 0.5, 0.5 + 0.25, 100)
add_note(piano_instrument, 76, 0.5, 0.5 + 0.25, 100)

# Bar 2: beat 4 (1.0s)
add_note(piano_instrument, 62, 1.0, 1.0 + 0.25, 100)
add_note(piano_instrument, 67, 1.0, 1.0 + 0.25, 100)
add_note(piano_instrument, 74, 1.0, 1.0 + 0.25, 100)
add_note(piano_instrument, 76, 1.0, 1.0 + 0.25, 100)

# Bar 3: beat 2 (2.5s)
add_note(piano_instrument, 62, 2.5, 2.5 + 0.25, 100)
add_note(piano_instrument, 67, 2.5, 2.5 + 0.25, 100)
add_note(piano_instrument, 74, 2.5, 2.5 + 0.25, 100)
add_note(piano_instrument, 76, 2.5, 2.5 + 0.25, 100)

# Bar 3: beat 4 (3.0s)
add_note(piano_instrument, 62, 3.0, 3.0 + 0.25, 100)
add_note(piano_instrument, 67, 3.0, 3.0 + 0.25, 100)
add_note(piano_instrument, 74, 3.0, 3.0 + 0.25, 100)
add_note(piano_instrument, 76, 3.0, 3.0 + 0.25, 100)

# Bar 4: beat 2 (4.5s)
add_note(piano_instrument, 62, 4.5, 4.5 + 0.25, 100)
add_note(piano_instrument, 67, 4.5, 4.5 + 0.25, 100)
add_note(piano_instrument, 74, 4.5, 4.5 + 0.25, 100)
add_note(piano_instrument, 76, 4.5, 4.5 + 0.25, 100)

# Bar 4: beat 4 (5.0s)
add_note(piano_instrument, 62, 5.0, 5.0 + 0.25, 100)
add_note(piano_instrument, 67, 5.0, 5.0 + 0.25, 100)
add_note(piano_instrument, 74, 5.0, 5.0 + 0.25, 100)
add_note(piano_instrument, 76, 5.0, 5.0 + 0.25, 100)

# Sax melody: 4-bar intro with a motif
# Bar 1: No sax
# Bar 2: Start of motif
add_note(sax_instrument, 65, 1.0, 1.125, 110)  # D
add_note(sax_instrument, 68, 1.125, 1.25, 110)  # F#
add_note(sax_instrument, 72, 1.25, 1.375, 110)  # A
add_note(sax_instrument, 76, 1.375, 1.5, 110)  # C

# Bar 3: Echo of motif
add_note(sax_instrument, 72, 2.0, 2.125, 110)
add_note(sax_instrument, 68, 2.125, 2.25, 110)
add_note(sax_instrument, 65, 2.25, 2.375, 110)
add_note(sax_instrument, 62, 2.375, 2.5, 110)

# Bar 4: Resolution
add_note(sax_instrument, 65, 3.0, 3.125, 110)  # D
add_note(sax_instrument, 68, 3.125, 3.25, 110)  # F#
add_note(sax_instrument, 72, 3.25, 3.375, 110)  # A
add_note(sax_instrument, 76, 3.375, 3.5, 110)  # C

# Add instruments to the PrettyMIDI object
pm.instruments.append(sax_instrument)
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drum_instrument)

# Write to a MIDI file
pm.write("dante_russo_intro.mid")
