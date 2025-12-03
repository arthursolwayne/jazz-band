
import pretty_midi

# Create a new MIDI file at 160 BPM (quarter note = 0.375s)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Set up the drum pattern for Bar 1 (1.5 seconds)
for bar in range(1):
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    for beat in [0, 2]:  # beats 1 and 3
        note = pretty_midi.Note(
            velocity=80,
            pitch=36,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.375
        )
        drums.notes.append(note)
    for beat in [1, 3]:  # beats 2 and 4
        note = pretty_midi.Note(
            velocity=80,
            pitch=38,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.375
        )
        drums.notes.append(note)
    for eighth in range(8):  # hihat on every eighth
        note = pretty_midi.Note(
            velocity=80,
            pitch=42,
            start=bar * 1.5 + eighth * 0.1875,
            end=bar * 1.5 + eighth * 0.1875 + 0.1875
        )
        drums.notes.append(note)

# Bar 2: Full Quartet (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
for beat in range(4):
    if beat == 0:
        note = pretty_midi.Note(
            velocity=80,
            pitch=50,  # D2 (root of Dm)
            start=1.5 + beat * 0.375,
            end=1.5 + beat * 0.375 + 0.375
        )
        bass.notes.append(note)
    elif beat == 1:
        note = pretty_midi.Note(
            velocity=80,
            pitch=53,  # F2 (fifth of Dm)
            start=1.5 + beat * 0.375,
            end=1.5 + beat * 0.375 + 0.375
        )
        bass.notes.append(note)
    elif beat == 2:
        note = pretty_midi.Note(
            velocity=80,
            pitch=49,  # C2 (chromatic approach below D2)
            start=1.5 + beat * 0.375,
            end=1.5 + beat * 0.375 + 0.375
        )
        bass.notes.append(note)
    elif beat == 3:
        note = pretty_midi.Note(
            velocity=80,
            pitch=50,  # D2 (root of Dm)
            start=1.5 + beat * 0.375,
            end=1.5 + beat * 0.375 + 0.375
        )
        bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
for note in [50, 53, 57, 60]:
    piano_note = pretty_midi.Note(
        velocity=90,
        pitch=note,
        start=1.5,
        end=3.0
    )
    piano.notes.append(piano_note)

# Bar 3: G7 (G B D F)
for note in [67, 71, 69, 65]:
    piano_note = pretty_midi.Note(
        velocity=90,
        pitch=note,
        start=3.0,
        end=4.5
    )
    piano.notes.append(piano_note)

# Bar 4: Cm7 (C Eb G Bb)
for note in [60, 63, 67, 68]:
    piano_note = pretty_midi.Note(
        velocity=90,
        pitch=note,
        start=4.5,
        end=6.0
    )
    piano.notes.append(piano_note)

# Sax: Short motif that sings — start, leave it hanging, come back and finish
# Motif: Dm (D F A C), but played as a short phrase
# Bar 2: Start the motif
note = pretty_midi.Note(
    velocity=100,
    pitch=50,  # D
    start=1.5,
    end=1.5 + 0.1875
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=53,  # F
    start=1.5 + 0.1875,
    end=1.5 + 0.375
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=57,  # A
    start=1.5 + 0.375,
    end=1.5 + 0.5625
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=60,  # C
    start=1.5 + 0.5625,
    end=1.5 + 0.75
)
sax.notes.append(note)

# Bar 3: Leave it hanging
note = pretty_midi.Note(
    velocity=100,
    pitch=50,  # D
    start=3.0,
    end=3.0 + 0.375
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=53,  # F
    start=3.0 + 0.375,
    end=3.0 + 0.75
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=57,  # A
    start=3.0 + 0.75,
    end=3.0 + 1.125
)
sax.notes.append(note)

# Bar 4: Come back and finish it
note = pretty_midi.Note(
    velocity=100,
    pitch=60,  # C
    start=4.5,
    end=4.5 + 0.1875
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=57,  # A
    start=4.5 + 0.1875,
    end=4.5 + 0.375
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=53,  # F
    start=4.5 + 0.375,
    end=4.5 + 0.5625
)
sax.notes.append(note)

note = pretty_midi.Note(
    velocity=100,
    pitch=50,  # D
    start=4.5 + 0.5625,
    end=4.5 + 0.75
)
sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
