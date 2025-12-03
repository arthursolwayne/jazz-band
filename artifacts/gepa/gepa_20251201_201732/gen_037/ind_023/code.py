
import pretty_midi
import numpy as np

# Set the tempo (160 BPM)
tempo = 160

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)
midi.time_signature_changes = [time_signature]

# Key signature: F major (no sharps or flats)
key_signature = pretty_midi.KeySignature(key_number=1, time=0.0)
midi.key_signature_changes = [key_signature]

# Time per bar (in seconds)
bar_time = 60.0 / tempo * 4  # 4/4 time
bar_duration = bar_time  # 6 seconds for 4 bars

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Using piano for drums

# Initialize instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)
drums = pretty_midi.Instrument(program=drum_program, is_drum=True)

# ------------------------------
# BAR 1: Little Ray on Drums
# ------------------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def make_drums(time_start, beat_duration):
    kick_notes = [36]  # C2
    snare_notes = [38]  # D2
    hihat_notes = [42]  # G#2

    # hihat on every eighth note
    for i in range(8):
        time = time_start + i * beat_duration / 2
        note = pretty_midi.Note(velocity=60, pitch=hihat_notes[0], start=time, end=time + 0.05)
        drums.notes.append(note)

    # Kick on 1 and 3 (first and third beat)
    for i in [0, 2]:
        time = time_start + i * beat_duration
        note = pretty_midi.Note(velocity=80, pitch=kick_notes[0], start=time, end=time + 0.1)
        drums.notes.append(note)

    # Snare on 2 and 4 (second and fourth beat)
    for i in [1, 3]:
        time = time_start + i * beat_duration
        note = pretty_midi.Note(velocity=85, pitch=snare_notes[0], start=time, end=time + 0.1)
        drums.notes.append(note)

make_drums(0.0, bar_time / 4)

# ------------------------------
# BAR 2: Full Band In
# ------------------------------
# Time for Bar 2
bar_start = bar_time

# Marcus (Bass) - Walking line in F (D2-G2, MIDI 38-43)
# F major -> F, Gm7, Am7, Bb7
# Bass line: F (C4), Gm7 (D2), Am7 (F2), Bb7 (A2)
def make_bass_line(time_start, beat_duration):
    # F -> D2 (root), chromatic approach to Gm7
    note = pretty_midi.Note(velocity=80, pitch=50, start=time_start, end=time_start + beat_duration)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=51, start=time_start + beat_duration, end=time_start + 2 * beat_duration)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=49, start=time_start + 2 * beat_duration, end=time_start + 3 * beat_duration)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=49, start=time_start + 3 * beat_duration, end=time_start + 4 * beat_duration)
    bass.notes.append(note)

make_bass_line(bar_start, bar_time / 4)

# Diane (Piano) - Open voicings, different chord each bar, resolve on last beat
def make_piano_chord(time_start, beat_duration, chord):
    root = chord[0]
    seventh = chord[1]
    third = chord[2]
    fifth = chord[3]

    # Open voicing
    notes = [root + 4, root + 7, root + 9, root + 11]  # F, A, C, D
    # Add 7th
    if seventh != 0:
        notes.append(seventh)
    # Resolve on last beat
    note = pretty_midi.Note(velocity=85, pitch=notes[-1], start=time_start + 3 * beat_duration, end=time_start + 4 * beat_duration)
    piano.notes.append(note)

    # Play the chord on beat 2
    for p in notes:
        note = pretty_midi.Note(velocity=85, pitch=p, start=time_start + beat_duration, end=time_start + beat_duration + 0.5)
        piano.notes.append(note)

# Fmaj7, Gm7, Am7, Bb7
chords = [
    [65, 72, 67, 69],  # Fmaj7: F, A, C, D
    [67, 74, 70, 72],  # Gm7: G, Bb, D, F
    [69, 76, 72, 74],  # Am7: A, C, E, G
    [71, 78, 74, 76]   # Bb7: Bb, D, F, Ab
]

for i, chord in enumerate(chords):
    make_piano_chord(bar_start, bar_time / 4, chord)

# You (Tenor Sax) - Motif: Start it, leave it hanging, return and finish it
def make_sax_melody(time_start, beat_duration):
    # Start with a phrase in C7 (G4), E6 (E6), F5 (F5), D5 (D5), leave hanging
    note = pretty_midi.Note(velocity=90, pitch=71, start=time_start, end=time_start + 0.5)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=76, start=time_start + 0.5, end=time_start + 1.0)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=76, start=time_start + 1.0, end=time_start + 1.5)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=72, start=time_start + 1.5, end=time_start + 2.0)
    sax.notes.append(note)
    # Return and finish it
    note = pretty_midi.Note(velocity=90, pitch=73, start=time_start + 2.0, end=time_start + 2.5)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=76, start=time_start + 2.5, end=time_start + 3.0)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=71, start=time_start + 3.0, end=time_start + 3.5)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=76, start=time_start + 3.5, end=time_start + 4.0)
    sax.notes.append(note)

make_sax_melody(bar_start, bar_time / 4)

# Add all instruments to the MIDI file
midi.instruments = [bass, piano, sax, drums]

# Save the MIDI file
# midi.write disabled
