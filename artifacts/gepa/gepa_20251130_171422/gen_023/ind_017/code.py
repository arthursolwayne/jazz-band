
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Using piano for drum samples
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Time Per Bar (160 BPM, 4/4 time)
BPM = 160
notes_per_beat = 4  # quarter note = 1 beat
ticks_per_beat = pm.resolution
time_per_beat = pretty_midi.utilities.seconds_to_time(ticks_per_beat, BPM)
time_per_bar = time_per_beat * 4  # 4 beats per bar

# Bar 1: Little Ray on drums (drum kit)
# We’ll use a simple pattern: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

def add_drums():
    # Kick on beat 1 and 3
    kick_notes = [(0, 36, 100), (time_per_beat * 2, 36, 100)]
    for time, note, velocity in kick_notes:
        drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

    # Snare on beat 2 and 4
    snare_notes = [(time_per_beat, 38, 100), (time_per_beat * 3, 38, 100)]
    for time, note, velocity in snare_notes:
        drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

    # Hihat on every eighth note
    for i in range(8):
        time = time_per_beat * i / 2
        hihat = 42
        drums.notes.append(pretty_midi.Note(velocity=70, pitch=hihat, start=time, end=time + 0.1))

add_drums()

# Bar 2-4: Everyone in
# Key: F major

# Bass (Marcus): Walking line, chromatic approaches, no repetition
def add_bass():
    # F -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> F (with chromatic approaches)
    bass_notes = [
        (time_per_beat, 65, 80),  # F
        (time_per_beat * 1.25, 67, 80),  # G
        (time_per_beat * 1.5, 66, 80),  # Ab
        (time_per_beat * 1.75, 69, 80),  # A
        (time_per_beat * 2, 67, 80),  # Bb
        (time_per_beat * 2.25, 71, 80),  # B
        (time_per_beat * 2.5, 72, 80),  # C
        (time_per_beat * 2.75, 74, 80),  # D
        (time_per_beat * 3, 69, 80),  # Eb
        (time_per_beat * 3.25, 65, 80),  # F
    ]
    for time, note, velocity in bass_notes:
        bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

add_bass()

# Diane on piano: 7th chords, on 2 and 4
def add_piano():
    # F7 (F A C E) on beat 2
    chord_notes = [53, 58, 60, 64]
    piano_notes = [(time_per_beat * 1, n, 90) for n in chord_notes]
    for time, note, velocity in piano_notes:
        piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.2))

    # G7 (G B D F) on beat 4
    chord_notes = [55, 59, 62, 65]
    piano_notes = [(time_per_beat * 3, n, 90) for n in chord_notes]
    for time, note, velocity in piano_notes:
        piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.2))

    # Add a slight chromatic passing tone on beat 3
    piano.notes.append(pretty_midi.Note(velocity=70, pitch=63, start=time_per_beat * 2.5, end=time_per_beat * 2.75))

add_piano()

# You on sax: A short, singable motif
def add_sax():
    # The motif: A - Bb - C - D - C - Bb - A - Bb
    # Notes in F major: A = 69, Bb = 67, C = 72, D = 74
    motif_pitches = [69, 67, 72, 74, 72, 67, 69, 67]
    motif_durations = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
    start_time = time_per_beat * 1  # starts on the 'and' of 2 (beat 1.5)
    for i, pitch in enumerate(motif_pitches):
        start = start_time + (i * 0.25)
        end = start + 0.25
        sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

add_sax()

# Save the MIDI
pm.write('jazz_intro.mid')
print("MIDI file created: jazz_intro.mid")
