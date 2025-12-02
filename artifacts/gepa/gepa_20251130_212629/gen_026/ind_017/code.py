
import pretty_midi

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes = [time_signature]

# Create instruments
drums = pretty_midi.Instrument(program=10)
piano = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
sax = pretty_midi.Instrument(program=64)

# Add instruments to the MIDI file
midi.instruments = [drums, piano, bass, sax]

# BPM = 160 => beats per second = 160 / 60 ≈ 2.6667
# 4 bars = 16 beats at 160 BPM → 6 seconds total
# Each beat = 0.375 seconds (60 / 160), each bar = 1.5 seconds
beat = 0.375

# Drum pattern for Bar 1 (Little Ray alone)
drum_notes = [
    (pretty_midi.note_number_to_name(36), beat * 0.0),  # Kick on beat 1
    (pretty_midi.note_number_to_name(38), beat * 0.5),  # Snare on beat 2
    (pretty_midi.note_number_to_name(42), beat * 0.0),  # Hihat on 1
    (pretty_midi.note_number_to_name(42), beat * 0.5),  # Hihat on 2
    (pretty_midi.note_number_to_name(42), beat * 1.0),  # Hihat on 3
    (pretty_midi.note_number_to_name(42), beat * 1.5),  # Hihat on 4
]

for note, time in drum_notes:
    note_number = pretty_midi.note_name_to_number(note)
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    drums.notes.append(note)

# Piano (Diane) comping on 2 and 4 of Bars 2-4
def add_piano_notes(bar_start, time):
    # 7th chords: F7 (F, A, C, E♭)
    # Fm7: F, Ab, C, Eb
    # Here we'll use F7 for tension
    chord_notes = [pretty_midi.note_name_to_number('F'), pretty_midi.note_name_to_number('A'),
                   pretty_midi.note_name_to_number('C'), pretty_midi.note_name_to_number('Eb')]
    for note in chord_notes:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + time, end=bar_start + time + 0.1)
        piano.notes.append(piano_note)

# Bass line by Marcus (chromatic walking line)
def add_bass_notes():
    # Start at F (Fm root), walk chromatically
    # Bb → B → C → C#
    # Each note on downbeats (1, 2, 3, 4), but we'll add chromatic passing tones
    bass_notes = [
        pretty_midi.note_name_to_number('F'),  # Beat 1
        pretty_midi.note_name_to_number('Bb'), # Beat 2
        pretty_midi.note_name_to_number('B'),  # Beat 3
        pretty_midi.note_name_to_number('C'),  # Beat 4
        pretty_midi.note_name_to_number('C#'), # Beat 5 (passing tone)
    ]
    for i, note in enumerate(bass_notes):
        start_time = i * beat
        bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + 0.1)
        bass.notes.append(bass_note)

# Sax solo (Dante) – 4-bar intro, bar 1 is drums only
# Bar 2-4: sax melody with space and tension

def add_sax_line():
    # Bar 2: Start of melody
    sax_notes = [
        (pretty_midi.note_name_to_number('F'), beat * 2.0),  # F (beat 1 of bar 2)
        (pretty_midi.note_name_to_number('Ab'), beat * 2.5),  # Ab (beat 2 of bar 2)
        (pretty_midi.note_name_to_number('C'), beat * 3.0),   # C (beat 3 of bar 2)
        (pretty_midi.note_name_to_number('Eb'), beat * 4.0),  # Eb (beat 4 of bar 2)
        (pretty_midi.note_name_to_number('F'), beat * 4.5),   # F (beat 1 of bar 3)
        (pretty_midi.note_name_to_number('Bb'), beat * 5.0),  # Bb (beat 2 of bar 3)
        (pretty_midi.note_name_to_number('C'), beat * 5.5),   # C (beat 3 of bar 3)
        (pretty_midi.note_name_to_number('Eb'), beat * 6.0),  # Eb (beat 4 of bar 3)
        (pretty_midi.note_name_to_number('F'), beat * 6.5),   # F (beat 1 of bar 4)
        (pretty_midi.note_name_to_number('Ab'), beat * 7.0),  # Ab (beat 2 of bar 4)
        (pretty_midi.note_name_to_number('Bb'), beat * 7.5),  # Bb (beat 3 of bar 4)
        (pretty_midi.note_name_to_number('C'), beat * 8.0),   # C (beat 4 of bar 4)
    ]

    for note, time in sax_notes:
        sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        sax.notes.append(sax_note)

# Add piano chords on 2 and 4 of bars 2-4
for bar in range(2, 5):
    add_piano_notes(bar * beat, 0.5)  # On 2
    add_piano_notes(bar * beat, 1.5)  # On 4

# Add the bass line
add_bass_notes()

# Add sax line
add_sax_line()

# Save the MIDI file
midi.write("jazz_intro_Fm.mid")
