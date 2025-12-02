
import pretty_midi
import numpy as np

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)  # 160 BPM

# Set key to F major
midi.key_signature = pretty_midi.KeySignature(key_number=1)  # F major

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Set up timing
time_per_beat = 60.0 / 160  # seconds per beat (60 seconds in a minute)
time_per_bar = time_per_beat * 4  # 4/4 time
time_per_eighth = time_per_beat / 2
time_per_sixteenth = time_per_beat / 4

# DRUMS: Bar 1 - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(bar_start):
    kicks = [bar_start + time_per_beat * i for i in [0, 2]]
    snares = [bar_start + time_per_beat * i for i in [1, 3]]
    hihats = [bar_start + time_per_sixteenth * i for i in range(8)]

    for t in kicks:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.05)
        drums.notes.append(note)
    for t in snares:
        note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.05)
        drums.notes.append(note)
    for t in hihats:
        note = pretty_midi.Note(velocity=75, pitch=42, start=t, end=t + 0.03)
        drums.notes.append(note)

# Add drums for bar 1
add_drums(0.0)

# BASS: Bar 1 - Walking line, chromatic approaches, no repeated notes
def add_bass(bar_start):
    # Start on F (65) with chromatic approach to E (64)
    notes = [
        (64, bar_start + 0.0),
        (65, bar_start + 0.25),
        (67, bar_start + 0.5),
        (69, bar_start + 0.75),
        (71, bar_start + 1.0),
        (69, bar_start + 1.25),
        (67, bar_start + 1.5),
        (65, bar_start + 1.75),
    ]
    for pitch, start in notes:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
        bass.notes.append(note)

# Add bass for bar 1
add_bass(0.0)

# SAX: Bar 1 - Rest
# Bar 2-4: Melody motif (start, leave hanging, come back)

def add_sax_melody(bar_start):
    # Motif in F major: F - G - Bb - F
    # Motif is played in bar 2, then rest in bar 3, then repeated in bar 4
    motif = [
        (65, bar_start + 0.0),  # F
        (67, bar_start + 0.25), # G
        (69, bar_start + 0.5),  # Bb
        (65, bar_start + 0.75), # F
    ]
    for pitch, start in motif:
        note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.25)
        sax.notes.append(note)

    # Repeat the motif in bar 4
    motif = [
        (65, bar_start + 3.0),  # F
        (67, bar_start + 3.25), # G
        (69, bar_start + 3.5),  # Bb
        (65, bar_start + 3.75), # F
    ]
    for pitch, start in motif:
        note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.25)
        sax.notes.append(note)

# Add sax melody in bar 2 and 4
add_sax_melody(1.5)  # Bar 2 starts at 1.5 seconds

# PIANO: Bar 2-4 - 7th chords, comp on 2 and 4, emotional shading
def add_piano(bar_start):
    # F7 (F, A, C, E), Bb7 (Bb, D, F, Ab), Eb7 (Eb, G, Bb, Db), F7
    chords = [
        (65, 69, 72, 68),  # F7
        (62, 67, 69, 64),  # Bb7
        (60, 67, 69, 62),  # Eb7
        (65, 69, 72, 68),  # F7
    ]

    # Time positions: 2 and 4 of each bar
    time_positions = [bar_start + 1.0, bar_start + 3.0]

    for i, chord in enumerate(chords):
        for t in time_positions:
            for pitch in chord:
                note = pretty_midi.Note(
                    velocity=95,  # "Angry" but subtle
                    pitch=pitch,
                    start=t,
                    end=t + 0.25
                )
                piano.notes.append(note)

# Add piano chords in bars 2-4
add_piano(1.5)  # Bar 2 starts at 1.5s

# DRUMS: Bars 2-4
def add_drums_bars_2_to_4():
    for bar in range(2, 5):
        bar_start = bar * time_per_bar
        add_drums(bar_start)

# Add drums in bars 2-4
add_drums_bars_2_to_4()

# BASS: Bars 2-4 - Walking lines, melodic phrasing
def add_bass_bars_2_to_4():
    bar_start = 1.5  # Bar 2 starts at 1.5s
    # Each bar is a walking line with chromatic approaches
    for i in range(2):
        bar = bar_start + i * time_per_bar
        notes = [
            (65, bar + 0.0),  # F
            (66, bar + 0.25), # F#
            (67, bar + 0.5),  # G
            (69, bar + 0.75), # Bb
            (71, bar + 1.0),  # B
            (69, bar + 1.25), # Bb
            (67, bar + 1.5),  # G
            (65, bar + 1.75), # F
        ]
        for pitch, start in notes:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
            bass.notes.append(note)

# Add bass lines for bars 2-3
add_bass_bars_2_to_4()

# Save the MIDI file
midi.write('dante_russo_intro.mid')
