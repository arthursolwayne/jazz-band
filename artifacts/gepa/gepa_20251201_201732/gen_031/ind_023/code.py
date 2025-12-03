
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI uses 0 for drums
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Definitions
BPM = 160
beat = 60.0 / BPM  # seconds per beat
bar = beat * 4  # 1.5s per bar
time = 0.0

# -------------------------------
# Drums: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Just hihat
# Bar 2-4: Full pattern

# Bar 1: Hihat only
for i in range(8):
    note = pretty_midi.Note(velocity=70, pitch=42, start=time + i * beat/2, end=time + i * beat/2 + 0.1)
    drums.notes.append(note)

# Bar 2-4: Full pattern
for bar_num in range(2, 5):
    time_start = bar * (bar_num - 1)
    for i in range(8):
        # Hihat
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time_start + i * beat/2, end=time_start + i * beat/2 + 0.1)
        drums.notes.append(hihat)
        # Kick on 1 and 3
        if i == 0 or i == 2:
            kick = pretty_midi.Note(velocity=100, pitch=36, start=time_start + i * beat/2, end=time_start + i * beat/2 + 0.1)
            drums.notes.append(kick)
        # Snare on 2 and 4
        if i == 1 or i == 3:
            snare = pretty_midi.Note(velocity=90, pitch=38, start=time_start + i * beat/2, end=time_start + i * beat/2 + 0.1)
            drums.notes.append(snare)

# -------------------------------
# Bass: Marcus - Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches

# Dm: Dm7 -> Gm7 -> Cm7 -> F7 (no modulation)
# Bar 1: Dm7
# Bar 2: Gm7
# Bar 3: Cm7
# Bar 4: F7

# Walk pattern: Root, b7, root, b7, root, b7, root, b7
pattern = [0, -1, 0, -1, 0, -1, 0, -1]

# Bar 1: Dm7 (root D2 = MIDI 38, b7 = C2 = MIDI 36)
for i in range(8):
    note = pretty_midi.Note(
        velocity=70,
        pitch=38 + pattern[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    bass.notes.append(note)

# Bar 2: Gm7 (root G2 = MIDI 43, b7 = F2 = MIDI 41)
time += bar
for i in range(8):
    note = pretty_midi.Note(
        velocity=70,
        pitch=43 + pattern[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    bass.notes.append(note)

# Bar 3: Cm7 (root C2 = MIDI 36, b7 = Bb2 = MIDI 34)
time += bar
for i in range(8):
    note = pretty_midi.Note(
        velocity=70,
        pitch=36 + pattern[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    bass.notes.append(note)

# Bar 4: F7 (root F2 = MIDI 39, b7 = Eb2 = MIDI 37)
time += bar
for i in range(8):
    note = pretty_midi.Note(
        velocity=70,
        pitch=39 + pattern[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    bass.notes.append(note)

# -------------------------------
# Piano: Diane - Open voicings, different chord each bar, resolve on last beat

# Bar 1: Dm7 (D, F, A, C)
chord1 = [38, 40, 43, 36]
for i in range(4):
    note = pretty_midi.Note(
        velocity=90,
        pitch=chord1[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    piano.notes.append(note)

# Bar 2: Gm7 (G, Bb, D, F)
chord2 = [43, 34, 38, 40]
for i in range(4):
    note = pretty_midi.Note(
        velocity=90,
        pitch=chord2[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    piano.notes.append(note)

# Bar 3: Cm7 (C, Eb, G, Bb)
chord3 = [36, 34, 43, 34]
for i in range(4):
    note = pretty_midi.Note(
        velocity=90,
        pitch=chord3[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    piano.notes.append(note)

# Bar 4: F7 (F, A, C, Eb)
chord4 = [39, 43, 36, 34]
for i in range(4):
    note = pretty_midi.Note(
        velocity=90,
        pitch=chord4[i],
        start=time + i * beat/2,
        end=time + i * beat/2 + 0.1
    )
    piano.notes.append(note)

# -------------------------------
# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: D (MIDI 38) -> Eb (MIDI 39) -> D (38) -> C (36)
# Play first two notes in bar 2, finish in bar 4

# Bar 2: D -> Eb
time = bar * 1  # start at bar 2
note1 = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.2)
note2 = pretty_midi.Note(velocity=100, pitch=39, start=time + 0.2, end=time + 0.4)
sax.notes.append(note1)
sax.notes.append(note2)

# Bar 4: D -> C
time = bar * 3  # start at bar 4
note3 = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.2)
note4 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.2, end=time + 0.4)
sax.notes.append(note3)
sax.notes.append(note4)

# Write the MIDI file
pm.write('dante_intro.mid')

print("MIDI file created: 'dante_intro.mid'")
