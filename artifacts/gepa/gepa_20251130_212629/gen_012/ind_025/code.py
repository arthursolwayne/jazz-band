
import pretty_midi
import numpy as np

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempos = [pretty_midi.TempoChange(160.0, 0)]

# Define key: Dm (D minor)
key = 'Dm'  # D minor (D, F, G, Bb, C, Eb, G)

# Define the 4-bar structure
# Bar 1: Drums only
# Bars 2-4: Full ensemble

# Create instruments
drums_program = pretty_midi.instrument_program('Drums')
bass_program = pretty_midi.instrument_program('Acoustic Bass')
piano_program = pretty_midi.instrument_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

midi.instruments = [drums, bass, piano, sax]

# Time in seconds per beat
beat = 60.0 / 160.0  # 0.375 seconds per beat
bar = 4 * beat  # 1.5 seconds per bar

# DRUMS - Bar 1
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(bar_start, beat):
    kicks = [1, 3]
    snares = [2, 4]
    hi_hats = [i + 0.125 for i in range(8)]

    for note in kicks:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=bar_start + (note - 1) * beat, end=bar_start + (note - 1) * beat + 0.1))

    for note in snares:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=bar_start + (note - 1) * beat, end=bar_start + (note - 1) * beat + 0.1))

    for note in hi_hats:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + (note - 1) * beat, end=bar_start + (note - 1) * beat + 0.1))

# BASS - Bar 1 (walking line)
def add_bass(bar_start, notes):
    for i, note in enumerate(notes):
        start = bar_start + i * beat
        end = start + 0.25
        bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# PIANO - Bars 2-4
def add_piano(bar_start, chords, durations):
    for i, (chord, duration) in enumerate(zip(chords, durations)):
        start = bar_start + i * beat
        end = start + duration
        for note in chord:
            piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# SAX - Bars 2-4
def add_sax(bar_start, notes, durations):
    for i, (note, duration) in enumerate(zip(notes, durations)):
        start = bar_start + i * beat
        end = start + duration
        sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# BAR 1: Drums only
add_drums(0.0, beat)

# BAR 2: Bass, Piano, Sax (intro motif starts here)
# Bass: Dm7 walking line (D, F, G, Bb, C, Eb, G)
# Dm7 = D, F, A, C
# Walking line: D -> F -> G -> Bb -> C -> Eb -> G
bass_line = [62, 65, 67, 70, 67, 69, 71]  # D, F, G, Bb, C, Eb, G
add_bass(beat, bass_line)

# Piano: Dm7 chord on 2 and 4
# Dm7 = [D, F, A, C] = 62, 65, 69, 67
# Comp on 2 and 4
piano_chords = [[62, 65, 69, 67], [62, 65, 69, 67]]
piano_durations = [2 * beat, 2 * beat]
add_piano(beat, piano_chords, piano_durations)

# Sax: "Motif" - D (62) -> F (65) -> G (67), leave it hanging
sax_notes = [62, 65, 67]
sax_durations = [0.5 * beat, 0.5 * beat, 0.5 * beat]
add_sax(beat, sax_notes, sax_durations)

# BAR 3: Continue with more piano, keep bass walking
# Bass continues
bass_line = [71, 69, 67, 65, 62, 60, 62]  # G, Eb, C, Bb, D, C, D
add_bass(2 * beat, bass_line)

# Piano: Dm7 again on 2 and 4
piano_chords = [[62, 65, 69, 67], [62, 65, 69, 67]]
piano_durations = [2 * beat, 2 * beat]
add_piano(2 * beat, piano_chords, piano_durations)

# Sax: Return to motif
sax_notes = [62, 65, 67]
sax_durations = [0.5 * beat, 0.5 * beat, 0.5 * beat]
add_sax(2 * beat, sax_notes, sax_durations)

# BAR 4: Full resolution
# Bass continues
bass_line = [67, 69, 71, 69, 67, 65, 62]  # C, Eb, G, Eb, C, Bb, D
add_bass(3 * beat, bass_line)

# Piano: Dm7 again
piano_chords = [[62, 65, 69, 67], [62, 65, 69, 67]]
piano_durations = [2 * beat, 2 * beat]
add_piano(3 * beat, piano_chords, piano_durations)

# Sax: Repeat motif with slight variation (G -> Bb)
sax_notes = [62, 65, 67, 70]  # D -> F -> G -> Bb
sax_durations = [0.5 * beat, 0.5 * beat, 0.5 * beat, 0.5 * beat]
add_sax(3 * beat, sax_notes, sax_durations)

# Save the MIDI file
midi.write("dante_russo_intro.mid")
