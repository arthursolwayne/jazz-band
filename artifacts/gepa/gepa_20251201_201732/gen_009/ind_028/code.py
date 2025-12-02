
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36] * 2
snare_notes = [38] * 2
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    time = bar1_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    time = bar1_start + (i * 0.75) + 0.25
    snare = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    time = bar1_start + (i * 0.375)
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D (MIDI 38) -> D# (MIDI 39) -> G (MIDI 43) -> G# (MIDI 44)
# Bar 3: A (MIDI 45) -> A# (MIDI 46) -> D (MIDI 38) -> D# (MIDI 39)
# Bar 4: G (MIDI 43) -> G# (MIDI 44) -> B (MIDI 49) -> C (MIDI 50)

bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

bar2_notes = [38, 39, 43, 44]
bar3_notes = [45, 46, 38, 39]
bar4_notes = [43, 44, 49, 50]

for i, pitch in enumerate(bar2_notes):
    time = bar2_start + (i * 0.375)
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

for i, pitch in enumerate(bar3_notes):
    time = bar3_start + (i * 0.375)
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

for i, pitch in enumerate(bar4_notes):
    time = bar4_start + (i * 0.375)
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: A7 (A, C#, E, G)
# Bar 4: G7 (G, B, D, F#)

bar2_piano_notes = [38, 43, 47, 51]
bar3_piano_notes = [45, 49, 53, 57]
bar4_piano_notes = [43, 47, 50, 53]

for i, pitch in enumerate(bar2_piano_notes):
    time = bar2_start + (i * 0.375)
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

for i, pitch in enumerate(bar3_piano_notes):
    time = bar3_start + (i * 0.375)
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

for i, pitch in enumerate(bar4_piano_notes):
    time = bar4_start + (i * 0.375)
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (MIDI 38), F# (MIDI 43), B (MIDI 49), A (MIDI 45)
# Bar 2: D -> F# -> B -> A
# Bar 3: D -> F# -> B -> rest
# Bar 4: A -> D -> F# -> B

bar2_sax_notes = [38, 43, 49, 45]
bar3_sax_notes = [38, 43, 49, 43]
bar4_sax_notes = [45, 38, 43, 49]

for i, pitch in enumerate(bar2_sax_notes):
    time = bar2_start + (i * 0.375)
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

for i, pitch in enumerate(bar3_sax_notes):
    time = bar3_start + (i * 0.375)
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

for i, pitch in enumerate(bar4_sax_notes):
    time = bar4_start + (i * 0.375)
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
