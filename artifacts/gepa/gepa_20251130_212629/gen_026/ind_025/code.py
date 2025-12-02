
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key: F minor
key = 'Fm'

# Time resolution in seconds for the 4 bars
bpm = 160
beat = 60.0 / bpm  # seconds per beat
bar_length = beat * 4  # 4 beats per bar
total_length = bar_length * 4  # 4 bars

# Define instruments
instrument_drums = pretty_midi.Instrument(program=10, is_drum=True)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_sax = pretty_midi.Instrument(program=64)

# Add instruments to the PrettyMIDI object
pm.instruments = [instrument_drums, instrument_piano, instrument_bass, instrument_sax]

# -- Little Ray on Drums (Bar 1 only) --
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums():
    for bar in range(1):
        for beat in [0, 2]:  # Kick on 1 and 3
            time = bar * bar_length + beat * beat
            note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.1)
            instrument_drums.notes.append(note)
        for beat in [1, 3]:  # Snare on 2 and 4
            time = bar * bar_length + beat * beat
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            instrument_drums.notes.append(note)
        # Hihat on every eighth
        for eighth in range(8):
            time = bar * bar_length + (eighth * beat / 2)
            note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05)
            instrument_drums.notes.append(note)

# -- Diane on Piano (Bars 2-4) --
def add_piano():
    # Diane plays 7th chords on 2 and 4
    # Fm7 (F, Ab, C, Eb), Bb7 (Bb, D, F, Ab), etc.
    def play_chord(chord_notes, start_time):
        for note in chord_notes:
            n = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + 0.2)
            instrument_piano.notes.append(n)

    # Bar 2: Fm7 on beat 2
    play_chord([71, 79, 76, 69], 1 * bar_length + 1 * beat)

    # Bar 2: Bb7 on beat 4
    play_chord([73, 78, 71, 79], 1 * bar_length + 3 * beat)

    # Bar 3: Eb7 on beat 2
    play_chord([69, 76, 81, 79], 2 * bar_length + 1 * beat)

    # Bar 3: Gm7 on beat 4
    play_chord([76, 84, 79, 71], 2 * bar_length + 3 * beat)

    # Bar 4: Am7 on beat 2
    play_chord([81, 89, 84, 76], 3 * bar_length + 1 * beat)

    # Bar 4: D7 on beat 4
    play_chord([74, 79, 82, 76], 3 * bar_length + 3 * beat)

# -- Marcus on Bass (Bars 2-4) --
def add_bass():
    # Walking line with chromatic approaches
    # Start from Fm scale, F, Gb, Ab, A, Bb, B, C, Db
    # Bassline: F, Gb, Ab, A, Bb, B, C, Db, Eb, F
    bass_notes = [71, 69, 79, 81, 73, 76, 76, 71, 69, 79]
    for i in range(len(bass_notes)):
        time = (i / 4) * bar_length
        note = pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=time, end=time + 0.25)
        instrument_bass.notes.append(note)

# -- Dante on Sax (Bars 2-4) -- 
def add_sax():
    # Short motif: F -> Ab -> B -> C (rests and space)
    # Start on beat 1 of bar 2
    # Phrase: F (start), Ab, B, C (end)
    # Rests in between, leave it hanging

    # Bar 2, beat 1: F
    note = pretty_midi.Note(velocity=100, pitch=71, start=1 * bar_length, end=1 * bar_length + 0.25)
    instrument_sax.notes.append(note)

    # Bar 2, beat 2: Ab
    note = pretty_midi.Note(velocity=100, pitch=79, start=1 * bar_length + 1 * beat, end=1 * bar_length + 1 * beat + 0.25)
    instrument_sax.notes.append(note)

    # Bar 2, beat 3: B
    note = pretty_midi.Note(velocity=100, pitch=76, start=1 * bar_length + 2 * beat, end=1 * bar_length + 2 * beat + 0.25)
    instrument_sax.notes.append(note)

    # Bar 2, beat 4: C
    note = pretty_midi.Note(velocity=100, pitch=76, start=1 * bar_length + 3 * beat, end=1 * bar_length + 3 * beat + 0.1)
    instrument_sax.notes.append(note)

# -- Apply all instruments --
add_drums()
add_piano()
add_bass()
add_sax()

# Save the MIDI file
pm.write("door_before_the_song.mid")
