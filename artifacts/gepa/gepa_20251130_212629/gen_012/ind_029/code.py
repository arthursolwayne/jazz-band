
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: D major
# Create instruments
bass_program = Program(33)  # Acoustic Bass
piano_program = Program(0)  # Acoustic Grand Piano
drums_program = Program(9)  # Acoustic Drums
sax_program = Program(64)   # Tenor Saxophone

bass_instr = Instrument(program=bass_program)
piano_instr = Instrument(program=piano_program)
drums_instr = Instrument(program=drums_program)
sax_instr = Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments.append(bass_instr)
midi.instruments.append(piano_instr)
midi.instruments.append(drums_instr)
midi.instruments.append(sax_instr)

# BPM = 160, 4/4 time => beat duration = 0.375 seconds
beat = 0.375
bar = beat * 4

# Helper function to convert time to seconds
def to_seconds(time):
    return time * beat

# --- Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1 (time 0 to 4 beats)
drums_instr.notes.extend([
    Note(drum_notes['kick'], to_seconds(0), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(0), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(0.5), to_seconds(0.1)),
    Note(drum_notes['kick'], to_seconds(1), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(1), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(1.5), to_seconds(0.1)),
    Note(drum_notes['snare'], to_seconds(2), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(2), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(2.5), to_seconds(0.1)),
    Note(drum_notes['kick'], to_seconds(3), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(3), to_seconds(0.1)),
    Note(drum_notes['hihat'], to_seconds(3.5), to_seconds(0.1)),
])

# --- Bar 2: Everyone in, saxophone motif
# D major scale: D E F# G A B C#
# Motif: D - E - F# (rest) - A (rest) - B - C# (rest) - D
# Time: bar 2 starts at 4 beats

sax_notes = [
    Note(62, to_seconds(4), to_seconds(4.1)),  # D4
    Note(64, to_seconds(4.5), to_seconds(4.6)), # E4
    Note(66, to_seconds(5), to_seconds(5.1)),   # F#4
    Note(69, to_seconds(6.5), to_seconds(6.6)), # A4
    Note(71, to_seconds(7), to_seconds(7.1)),   # B4
    Note(72, to_seconds(8.5), to_seconds(8.6)), # C#5
    Note(62, to_seconds(9), to_seconds(9.1)),   # D4
]

sax_instr.notes.extend(sax_notes)

# --- Bar 2-3: Marcus on bass - walking line with chromatic approaches
# D major key, walking bass line with chromatic passing tones
# D - F - E - G - A - B - C# - D
# Time: bar 2 starts at 4 beats

bass_notes = [
    Note(45, to_seconds(4), to_seconds(4.1)),   # D3
    Note(47, to_seconds(4.5), to_seconds(4.6)), # F3
    Note(46, to_seconds(5), to_seconds(5.1)),   # E3
    Note(48, to_seconds(5.5), to_seconds(5.6)), # G3
    Note(49, to_seconds(6), to_seconds(6.1)),   # A3
    Note(50, to_seconds(6.5), to_seconds(6.6)), # B3
    Note(51, to_seconds(7), to_seconds(7.1)),   # C#3
    Note(45, to_seconds(7.5), to_seconds(7.6)), # D3
    Note(46, to_seconds(8), to_seconds(8.1)),   # E3
    Note(48, to_seconds(8.5), to_seconds(8.6)), # G3
    Note(49, to_seconds(9), to_seconds(9.1)),   # A3
]

bass_instr.notes.extend(bass_notes)

# --- Bar 2-4: Diane on piano - 7th chords on 2 and 4
# D7 on 2, A7 on 4, Bm7 on 4.5
# Time: bar 2 starts at 4 beats

# D7 chord: D F# A C#
# A7 chord: A C# E G
# Bm7 chord: B D F# A

piano_notes = [
    # D7 on beat 2 (beat 5.5)
    Note(62, to_seconds(5.5), to_seconds(5.6)),
    Note(66, to_seconds(5.5), to_seconds(5.6)),
    Note(69, to_seconds(5.5), to_seconds(5.6)),
    Note(72, to_seconds(5.5), to_seconds(5.6)),
    
    # A7 on beat 4 (beat 7.5)
    Note(69, to_seconds(7.5), to_seconds(7.6)),
    Note(72, to_seconds(7.5), to_seconds(7.6)),
    Note(74, to_seconds(7.5), to_seconds(7.6)),
    Note(77, to_seconds(7.5), to_seconds(7.6)),
    
    # Bm7 on beat 4.5 (beat 8)
    Note(71, to_seconds(8), to_seconds(8.1)),
    Note(64, to_seconds(8), to_seconds(8.1)),
    Note(66, to_seconds(8), to_seconds(8.1)),
    Note(69, to_seconds(8), to_seconds(8.1)),
]

piano_instr.notes.extend(piano_notes)

# --- Bar 4: Little Ray fills
# Add a fill at the end
drums_instr.notes.extend([
    Note(drum_notes['hihat'], to_seconds(9.5), to_seconds(9.6)),
    Note(drum_notes['snare'], to_seconds(9.75), to_seconds(9.85)),
    Note(drum_notes['kick'], to_seconds(10), to_seconds(10.1)),
    Note(drum_notes['hihat'], to_seconds(10), to_seconds(10.1)),
    Note(drum_notes['hihat'], to_seconds(10.5), to_seconds(10.6)),
])

# Write the MIDI file
midi.write('jazz_intro.mid')
