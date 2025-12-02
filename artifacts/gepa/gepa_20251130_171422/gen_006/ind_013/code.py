
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Tempo: 160 BPM
# 4/4 time
# 6 seconds per 4 bars

# Define note durations in seconds
beat = 0.375  # 60 / 160 = 0.375 seconds per beat
bar = beat * 4  # 1.5 seconds per bar

# -- DRUMS: Little Ray (Bar 1) --
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1
drum_notes = [
    (0, 36, 100, 0),  # Kick on beat 1
    (beat, 48, 100, 0),  # Snare on beat 2
    (beat * 2, 36, 100, 0),  # Kick on beat 3
    (beat * 3, 48, 100, 0),  # Snare on beat 4
    # Hi-hats every eighth
    (0, 42, 80, 0),
    (beat * 0.5, 42, 80, 0),
    (beat * 1, 42, 80, 0),
    (beat * 1.5, 42, 80, 0),
    (beat * 2, 42, 80, 0),
    (beat * 2.5, 42, 80, 0),
    (beat * 3, 42, 80, 0),
    (beat * 3.5, 42, 80, 0),
]

for time, note, velocity, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# -- BASS: Marcus (Bars 1-4) --
# Walking bass line with chromatic approaches, no repeated notes

# Dm7 = D F A C
# Tonic: D, dominant: F, 7th: C, 3rd: A

# Bar 1
bass_notes = [
    (0, 50, 80, 0.375),  # D
    (beat, 51, 80, 0.375),  # Eb (chromatic approach)
    (beat * 2, 52, 80, 0.375),  # F
    (beat * 3, 57, 80, 0.375),  # A
]

# Bar 2
bass_notes += [
    (beat * 4, 60, 80, 0.375),  # C
    (beat * 5, 59, 80, 0.375),  # Bb (chromatic approach)
    (beat * 6, 57, 80, 0.375),  # A
    (beat * 7, 52, 80, 0.375),  # F
]

# Bar 3
bass_notes += [
    (beat * 8, 50, 80, 0.375),  # D
    (beat * 9, 49, 80, 0.375),  # C# (chromatic approach)
    (beat * 10, 52, 80, 0.375),  # F
    (beat * 11, 57, 80, 0.375),  # A
]

# Bar 4
bass_notes += [
    (beat * 12, 60, 80, 0.375),  # C
    (beat * 13, 61, 80, 0.375),  # C#
    (beat * 14, 57, 80, 0.375),  # A
    (beat * 15, 52, 80, 0.375),  # F
]

for time, note, velocity, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)
    bass.notes.append(bass_note)

# -- PIANO: Diane (Bars 2-4) --
# 7th chords, comp on 2 and 4, 7th chords: Dm7, G7, Cm7, F7

# Bar 2: Dm7 = D F A C
piano_notes = [
    (beat * 1, 50, 80, 0.15),  # D
    (beat * 1, 55, 80, 0.15),  # F
    (beat * 1, 60, 80, 0.15),  # A
    (beat * 1, 62, 80, 0.15),  # C
]

# Bar 3: G7 = G B D F
piano_notes += [
    (beat * 3, 67, 80, 0.15),  # G
    (beat * 3, 71, 80, 0.15),  # B
    (beat * 3, 69, 80, 0.15),  # D
    (beat * 3, 67, 80, 0.15),  # F
]

# Bar 4: Cm7 = C Eb G Bb
piano_notes += [
    (beat * 5, 60, 80, 0.15),  # C
    (beat * 5, 64, 80, 0.15),  # Eb
    (beat * 5, 67, 80, 0.15),  # G
    (beat * 5, 65, 80, 0.15),  # Bb
]

# Bar 4: F7 = F A C E
piano_notes += [
    (beat * 7, 65, 80, 0.15),  # F
    (beat * 7, 70, 80, 0.15),  # A
    (beat * 7, 67, 80, 0.15),  # C
    (beat * 7, 69, 80, 0.15),  # E
]

for time, note, velocity, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)
    piano.notes.append(piano_note)

# -- SAX: You (Bars 2-4) --
# One short motif, make it sing. Start it, leave it hanging. Come back and finish.

# Dm7: D F A C

# Bar 2
sax_notes = [
    (beat * 1, 50, 100, 0.5),  # D
    (beat * 1.5, 55, 100, 0.5),  # F
    (beat * 2, 57, 100, 0.5),  # A
    (beat * 2.5, 60, 100, 0.5),  # C
]

# Bar 3
sax_notes += [
    (beat * 3, 55, 100, 0.5),  # F
    (beat * 3.5, 60, 100, 0.5),  # C
    (beat * 4, 57, 100, 0.5),  # A
    (beat * 4.5, 50, 100, 0.5),  # D
]

# Bar 4
sax_notes += [
    (beat * 5, 50, 100, 0.5),  # D
    (beat * 5.5, 55, 100, 0.5),  # F
    (beat * 6, 57, 100, 0.5),  # A
    (beat * 6.5, 60, 100, 0.5),  # C
]

for time, note, velocity, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + duration)
    sax.notes.append(sax_note)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Save the MIDI file
midi.save('wayne_intro.mid')
