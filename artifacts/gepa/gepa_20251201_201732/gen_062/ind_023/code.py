
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: Dm (D Dorian)
# Scale: D, E, F, G, A, B, C
# Chords: Dm7, Gm7, Cm7, F7
# Root movements: D → G → C → F (secondary dominants)

# Define the time in seconds per bar (BPM = 160, 4/4)
bar_length = 60.0 / 160 * 4  # 6 seconds per 4 bars

# Create instruments
bass_instrument = Instrument(program=33)  # Acoustic Bass
piano_instrument = Instrument(program=0)  # Acoustic Grand Piano
drums_instrument = Instrument(program=0)  # Drums
sax_instrument = Instrument(program=64)  # Tenor Saxophone

# Add instruments to the PrettyMIDI object
pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# ============= DRUMS =============

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(instrument, start_time):
    kick_notes = [Note(36, 100, start_time, start_time + 0.375),  # Kick on 1
                  Note(36, 100, start_time + 1.5, start_time + 1.5 + 0.375)]  # Kick on 3
    snare_notes = [Note(38, 100, start_time + 0.75, start_time + 0.75 + 0.375),  # Snare on 2
                   Note(38, 100, start_time + 2.25, start_time + 2.25 + 0.375)]  # Snare on 4
    hihat_notes = [Note(42, 80, start_time + i * 0.375, start_time + i * 0.375 + 0.125) for i in range(16)]  # Every eighth
    instrument.notes.extend(kick_notes)
    instrument.notes.extend(snare_notes)
    instrument.notes.extend(hihat_notes)

# Bar 1 only – intro
add_drums(drums_instrument, 0)

# ============= BASS =============

# Bar 1: Walking bass line (Dm7) - D2, G2, C2, F2
def add_bass_line(instrument, start_time, chord_notes, duration=0.375):
    for note in chord_notes:
        instrument.notes.append(Note(note, 60, start_time, start_time + duration))
        start_time += duration

# Bar 1: Dm7 (D, F, A, C) – walking line
bass_notes = [40, 43, 45, 47, 40, 41, 43, 44]  # D2, F2, A2, C2, D2, Eb2, F2, G2 (chromatic approach)
add_bass_line(bass_instrument, 0, bass_notes)

# ============= PIANO =============

# Bar 1: Open voicing, Dm7 (D, F, A, C)
# Bar 2: Gm7 (G, Bb, D, F)
# Bar 3: Cm7 (C, Eb, G, Bb)
# Bar 4: F7 (F, A, C, E)

def add_piano(instrument, start_time, chord_notes):
    # Open voicing with root, 7th, 3rd, 5th, spaced out
    for note in chord_notes:
        instrument.notes.append(Note(note, 90, start_time, start_time + 0.75))

# Bar 1: Dm7 (D, F, A, C) – 3rd inversion (C, D, F, A)
add_piano(piano_instrument, 0, [48, 50, 52, 55])

# Bar 2: Gm7 (G, Bb, D, F) – 3rd inversion (D, F, G, Bb)
add_piano(piano_instrument, 1.5, [55, 57, 59, 62])

# Bar 3: Cm7 (C, Eb, G, Bb) – 3rd inversion (G, Bb, C, Eb)
add_piano(piano_instrument, 3.0, [62, 64, 65, 67])

# Bar 4: F7 (F, A, C, E) – 3rd inversion (C, E, F, A)
add_piano(piano_instrument, 4.5, [60, 64, 65, 68])

# ============= SAX =============

# Your motif: Dm7 (D, F, A, C)
# Motif: D (beat 1), F (beat 2), A (beat 3), C (beat 4) – then leave it hanging
# Motif: D, F, A, C, (rest) – build tension

def add_sax(instrument, start_time, notes):
    for i, note in enumerate(notes):
        instrument.notes.append(Note(note, 100, start_time + i * 0.375, start_time + i * 0.375 + 0.375))

# Bar 1: D, F, A, C (beat 1-4)
add_sax(sax_instrument, 0, [50, 52, 55, 57])

# No continuation – leave it hanging

# ============= EXPORT =============

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
