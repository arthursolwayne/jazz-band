
import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D major
key = 'D'

# Create instruments
instrument_drums = pretty_midi.Instrument(program=10)  # Drums
instrument_piano = pretty_midi.Instrument(program=0)   # Piano
instrument_bass = pretty_midi.Instrument(program=33)   # Electric Bass
instrument_sax = pretty_midi.Instrument(program=64)    # Tenor Saxophone

# Add instruments to the MIDI
midi.instruments = [instrument_drums, instrument_piano, instrument_bass, instrument_sax]

# Create a time signature (4/4)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes = [time_signature]

# BPM is already set

# Define note durations in seconds
beat = 0.375  # At 160 BPM, 1 beat = 0.375 seconds
bar = 4 * beat  # 1.5 seconds per bar

# Function to convert MIDI note number to note name (for debugging)
def note_number_to_name(note_number):
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = (note_number - 12) // 12 - 1
    note = note_names[(note_number - 12) % 12]
    return f"{note}{octave}"

# ---------------------
# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Note: 60 is C3, 48 is C2, 42 is G2
# Frequencies for reference: C2 (65.41Hz), G2 (98.00Hz), C3 (130.81Hz)

# Kick on beats 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=48, start=0, end=beat),
              pretty_midi.Note(velocity=100, pitch=48, start=2*beat, end=3*beat)]

# Snare on beats 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=60, start=beat, end=2*beat),
               pretty_midi.Note(velocity=100, pitch=60, start=3*beat, end=4*beat)]

# Hihat on every eighth note
hihat_notes = []
for i in range(0, 4):
    for j in range(0, 2):
        hihat_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i*beat + j*beat/2, end=i*beat + j*beat/2 + beat/4))

# Add to drums instrument
instrument_drums.notes.extend(kick_notes)
instrument_drums.notes.extend(snare_notes)
instrument_drums.notes.extend(hihat_notes)

# ---------------------
# Bar 2: Diane on piano — 7th chords, comp on 2 and 4

# D7 chord: D, F#, A, C
# D = 62, F# = 66, A = 69, C = 60
# Play on beat 2 and 4

# D7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=beat, end=beat + beat/4),
    pretty_midi.Note(velocity=100, pitch=66, start=beat, end=beat + beat/4),
    pretty_midi.Note(velocity=100, pitch=69, start=beat, end=beat + beat/4),
    pretty_midi.Note(velocity=100, pitch=60, start=beat, end=beat + beat/4),
]

# D7 on beat 4
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3*beat, end=3*beat + beat/4),
    pretty_midi.Note(velocity=100, pitch=66, start=3*beat, end=3*beat + beat/4),
    pretty_midi.Note(velocity=100, pitch=69, start=3*beat, end=3*beat + beat/4),
    pretty_midi.Note(velocity=100, pitch=60, start=3*beat, end=3*beat + beat/4),
])

instrument_piano.notes.extend(piano_notes)

# ---------------------
# Bar 2: Marcus on bass — walking line, chromatic approaches, never the same note twice

# Start on D (62), walk up (chromatic) for 4 beats
# D (62) -> D# (63) -> E (64) -> F (65)
# Then back down on beat 4

bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=0, end=beat),     # D
    pretty_midi.Note(velocity=100, pitch=63, start=beat, end=2*beat), # D#
    pretty_midi.Note(velocity=100, pitch=64, start=2*beat, end=3*beat), # E
    pretty_midi.Note(velocity=100, pitch=65, start=3*beat, end=4*beat), # F
]

instrument_bass.notes.extend(bass_notes)

# ---------------------
# Bar 2-4: Dante on tenor sax — one short motif, make it sing

# D (62), F# (66), A (69), and back to D (62)
# Play on beats 2 and 4 in bars 2 and 3, with a space in the middle

# Bar 2, beat 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=beat, end=beat + beat/2),
    pretty_midi.Note(velocity=100, pitch=66, start=beat + beat/2, end=beat + beat),
]

# Bar 3, beat 2
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=beat*2 + beat/2, end=beat*2 + beat),
])

# Bar 4, beat 4 — back to D, but leave it hanging (half note)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3*beat, end=3*beat + beat),
])

instrument_sax.notes.extend(sax_notes)

# Write the MIDI file
midi.write("jazz_intro_d.midi")
