
import pretty_midi
import numpy as np

# Set up the tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create the Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(time_signature[0], time_signature[1]))

# Define key (F major)
key = 'F'

# Define instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
bass_instrument = pretty_midi.Instrument(program=33)  # Double Bass
piano_instrument = pretty_midi.Instrument(program=0)   # Acoustic Piano
drum_instrument = pretty_midi.Instrument(program=10)   # Drums

pm.instruments = [sax_instrument, bass_instrument, piano_instrument, drum_instrument]

# Time per beat (in seconds)
beat_time = 60.0 / tempo  # 0.375 seconds per beat
bar_time = beat_time * 4  # 1.5 seconds per bar

# Define the 4-bar sequence

# Bar 1: Drums only (snare on 2 and 4, kick on 1 and 3, hihat on every eighth)
def play_bar1_drums():
    bar_start = 0.0
    # Kick on 1 and 3
    note_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.05)
    note_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + beat_time * 2, end=bar_start + beat_time * 2 + 0.05)
    drum_instrument.notes.extend([note_kick_1, note_kick_3])
    
    # Snare on 2 and 4
    note_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat_time, end=bar_start + beat_time + 0.05)
    note_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + beat_time * 3, end=bar_start + beat_time * 3 + 0.05)
    drum_instrument.notes.extend([note_snare_2, note_snare_4])
    
    # Hi-hat on every eighth
    for i in range(8):
        note_hat = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * beat_time / 2, end=bar_start + i * beat_time / 2 + 0.02)
        drum_instrument.notes.append(note_hat)

# Bar 2: Bass walks, piano comps, sax begins
def play_bar2():
    bar_start = bar_time

    # Bass: F - G - A - Bb (walking line, roots and fifths with chromatic approaches)
    bass_notes = [
        pretty_midi.Note(velocity=90, pitch=71, start=bar_start, end=bar_start + 0.25),  # F3
        pretty_midi.Note(velocity=90, pitch=72, start=bar_start + 0.25, end=bar_start + 0.5),  # G3
        pretty_midi.Note(velocity=90, pitch=74, start=bar_start + 0.5, end=bar_start + 0.75),  # A3
        pretty_midi.Note(velocity=90, pitch=73, start=bar_start + 0.75, end=bar_start + 1.0),  # Bb3
    ]
    bass_instrument.notes.extend(bass_notes)

    # Piano: Fmaj7 on bar 2, resolving on beat 4
    # Open voicing: F (C4), A (C4+3), C (E4), E (G4)
    chord_notes = [
        pretty_midi.Note(velocity=80, pitch=60, start=bar_start, end=bar_start + 0.25),  # F4
        pretty_midi.Note(velocity=80, pitch=64, start=bar_start, end=bar_start + 0.25),  # A4
        pretty_midi.Note(velocity=80, pitch=67, start=bar_start, end=bar_start + 0.25),  # C5
        pretty_midi.Note(velocity=80, pitch=71, start=bar_start, end=bar_start + 0.25),  # E5
    ]
    piano_instrument.notes.extend(chord_notes)

    # Sax: motif begins
    sax_notes = [
        pretty_midi.Note(velocity=100, pitch=66, start=bar_start, end=bar_start + 0.25),  # B4
        pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.25, end=bar_start + 0.5),  # A4
        pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 0.5, end=bar_start + 0.75),  # G4
        pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 0.75, end=bar_start + 1.0),  # Bb4
    ]
    sax_instrument.notes.extend(sax_notes)

# Bar 3: Bass continues, piano comps, sax continues
def play_bar3():
    bar_start = bar_time * 2

    # Bass: G - A - Bb - C (walking line)
    bass_notes = [
        pretty_midi.Note(velocity=90, pitch=72, start=bar_start, end=bar_start + 0.25),  # G3
        pretty_midi.Note(velocity=90, pitch=74, start=bar_start + 0.25, end=bar_start + 0.5),  # A3
        pretty_midi.Note(velocity=90, pitch=73, start=bar_start + 0.5, end=bar_start + 0.75),  # Bb3
        pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 0.75, end=bar_start + 1.0),  # C4
    ]
    bass_instrument.notes.extend(bass_notes)

    # Piano: G7 on bar 3, resolving on beat 4
    # Open voicing: G (C4), B (C4+3), D (E4), F (G4)
    chord_notes = [
        pretty_midi.Note(velocity=80, pitch=62, start=bar_start, end=bar_start + 0.25),  # G4
        pretty_midi.Note(velocity=80, pitch=65, start=bar_start, end=bar_start + 0.25),  # B4
        pretty_midi.Note(velocity=80, pitch=67, start=bar_start, end=bar_start + 0.25),  # D5
        pretty_midi.Note(velocity=80, pitch=71, start=bar_start, end=bar_start + 0.25),  # F5
    ]
    piano_instrument.notes.extend(chord_notes)

    # Sax: motif continues (mirror previous, with space)
    sax_notes = [
        pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.5),  # G4
        pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 0.5, end=bar_start + 1.0),  # Bb4
    ]
    sax_instrument.notes.extend(sax_notes)

# Bar 4: Bass ends, piano resolves, sax finishes motif
def play_bar4():
    bar_start = bar_time * 3

    # Bass: A - Bb - C - D (walking line)
    bass_notes = [
        pretty_midi.Note(velocity=90, pitch=74, start=bar_start, end=bar_start + 0.25),  # A3
        pretty_midi.Note(velocity=90, pitch=73, start=bar_start + 0.25, end=bar_start + 0.5),  # Bb3
        pretty_midi.Note(velocity=90, pitch=76, start=bar_start + 0.5, end=bar_start + 0.75),  # C4
        pretty_midi.Note(velocity=90, pitch=77, start=bar_start + 0.75, end=bar_start + 1.0),  # D4
    ]
    bass_instrument.notes.extend(bass_notes)

    # Piano: A7 on bar 4, resolving on beat 4
    # Open voicing: A (C4), C (C4+3), E (E4), G (G4)
    chord_notes = [
        pretty_midi.Note(velocity=80, pitch=65, start=bar_start, end=bar_start + 0.25),  # A4
        pretty_midi.Note(velocity=80, pitch=68, start=bar_start, end=bar_start + 0.25),  # C5
        pretty_midi.Note(velocity=80, pitch=72, start=bar_start, end=bar_start + 0.25),  # E5
        pretty_midi.Note(velocity=80, pitch=76, start=bar_start, end=bar_start + 0.25),  # G5
    ]
    piano_instrument.notes.extend(chord_notes)

    # Sax: motif resolves
    sax_notes = [
        pretty_midi.Note(velocity=100, pitch=66, start=bar_start + 0.75, end=bar_start + 1.0),  # B4
    ]
    sax_instrument.notes.extend(sax_notes)

# Play all the bars
play_bar1_drums()
play_bar2()
play_bar3()
play_bar4()

# Save the MIDI file
pm.write("dante_intro.mid")
