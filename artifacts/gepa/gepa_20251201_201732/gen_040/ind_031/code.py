
import pretty_midi
from pretty_midi import Note, NoteList

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Time settings
bpm = 160
note_duration = 60.0 / bpm / 4  # Duration of a quarter note in seconds
bar_length = 4 * note_duration  # One bar = four quarter notes
total_length = 4 * bar_length  # Four bars total

# --- DRUMS (LITTLE RAY) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in range(4):
    for beat in range(4):
        time = bar * bar_length + beat * note_duration
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            drums.notes.append(Note(velocity=100, pitch=36, start=time, end=time + note_duration/2))
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            drums.notes.append(Note(velocity=100, pitch=38, start=time, end=time + note_duration/2))
        # Hihat on every 8th
        for eighth in range(2):
            hihat_time = time + (eighth * note_duration / 2)
            drums.notes.append(Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + note_duration/4))

# --- BASS (MARCUS) ---
# Walking line in F: Roots and fifths with chromatic approaches
# Start on F (F3 - MIDI 65) -> C (C4 - MIDI 60) -> G (G3 - MIDI 67) -> D (D3 - MIDI 62)
# Use chromatic approach to G
# Bar 1: F -> C -> G (chromatic approach)
# Bar 2: G -> D -> A
# Bar 3: A -> E -> B
# Bar 4: B -> F# -> C

bass_notes = [
    # Bar 1
    Note(velocity=90, pitch=65, start=0, end=note_duration),
    Note(velocity=90, pitch=60, start=note_duration, end=2*note_duration),
    Note(velocity=90, pitch=67, start=2*note_duration, end=3*note_duration),
    Note(velocity=90, pitch=66, start=2*note_duration, end=2.5*note_duration),  # chromatic approach to G

    # Bar 2
    Note(velocity=90, pitch=67, start=3*note_duration, end=4*note_duration),
    Note(velocity=90, pitch=62, start=4*note_duration, end=5*note_duration),
    Note(velocity=90, pitch=69, start=5*note_duration, end=6*note_duration),
    Note(velocity=90, pitch=68, start=5*note_duration, end=5.5*note_duration),  # chromatic approach to A

    # Bar 3
    Note(velocity=90, pitch=69, start=6*note_duration, end=7*note_duration),
    Note(velocity=90, pitch=64, start=7*note_duration, end=8*note_duration),
    Note(velocity=90, pitch=71, start=8*note_duration, end=9*note_duration),
    Note(velocity=90, pitch=70, start=8*note_duration, end=8.5*note_duration),  # chromatic approach to B

    # Bar 4
    Note(velocity=90, pitch=71, start=9*note_duration, end=10*note_duration),
    Note(velocity=90, pitch=67, start=10*note_duration, end=11*note_duration),
    Note(velocity=90, pitch=72, start=11*note_duration, end=12*note_duration),
    Note(velocity=90, pitch=71, start=11*note_duration, end=11.5*note_duration),  # chromatic approach to C
]

bass.notes.extend(bass_notes)

# --- PIANO (DIANE) ---
# Open voicings, resolve on the last beat of each bar

# Bar 1: Fmaj7 (F, A, C, E) -> C7 (C, E, G, Bb) -> Gm7 (G, Bb, D, F) -> Amaj7 (A, C#, E, G#)
# But in F, so Amaj7 would be A, C, E, G

bar1_chords = [
    [65, 68, 72, 69],  # Fmaj7
    [72, 69, 76, 70],  # C7
    [76, 70, 67, 65],  # Gm7
    [69, 72, 76, 79],  # Amaj7
]

bar2_chords = [
    [76, 70, 77, 69],  # G7
    [69, 72, 76, 79],  # Amaj7
    [79, 72, 76, 74],  # Bm7
    [72, 76, 79, 82],  # Cmaj7
]

bar3_chords = [
    [79, 72, 76, 74],  # Bm7
    [72, 76, 79, 82],  # Cmaj7
    [82, 76, 81, 79],  # Dm7
    [76, 79, 82, 85],  # Emaj7
]

bar4_chords = [
    [82, 76, 81, 79],  # Dm7
    [76, 79, 82, 85],  # Emaj7
    [85, 79, 84, 82],  # Fm7
    [79, 82, 85, 88],  # Gmaj7
]

# Add notes to piano, only on beat 2 and 4, with one note per chord
def add_piano_notes(chords, offset):
    for i, chord in enumerate(chords):
        if i % 2 == 1:  # only on beat 2 and 4
            time = offset + (i // 2) * bar_length
            for pitch in chord:
                piano.notes.append(Note(velocity=100, pitch=pitch, start=time, end=time + note_duration / 2))

add_piano_notes(bar1_chords, 0)
add_piano_notes(bar2_chords, bar_length)
add_piano_notes(bar3_chords, 2 * bar_length)
add_piano_notes(bar4_chords, 3 * bar_length)

# --- SAX (YOU) ---
# Short motif: F (65) -> A (68) -> G (67) -> rest (0.5 beat) -> F (65) -> G (67) -> A (68)
# Leave it hanging on the last A

sax_notes = [
    Note(velocity=110, pitch=65, start=0, end=note_duration),
    Note(velocity=110, pitch=68, start=note_duration, end=2 * note_duration),
    Note(velocity=110, pitch=67, start=2 * note_duration, end=3 * note_duration),
    Note(velocity=110, pitch=65, start=3.5 * note_duration, end=4.5 * note_duration),
    Note(velocity=110, pitch=67, start=4.5 * note_duration, end=5.5 * note_duration),
    Note(velocity=110, pitch=68, start=5.5 * note_duration, end=6 * note_duration),
]

sax.notes.extend(sax_notes)

# Save MIDI file
pm.write("jazz_intro_wayne.mid")

print("MIDI file 'jazz_intro_wayne.mid' has been generated.")
