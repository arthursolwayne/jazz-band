
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    time = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.0, end=time + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.125, end=time + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D (38) -> Eb (39) -> G (43) -> A (45)
# Bar 3: Bb (42) -> B (43) -> D (38) -> Eb (39)
# Bar 4: G (43) -> A (45) -> B (43) -> D (38)
bar_times = [1.5, 3.0, 4.5]
for i, time in enumerate(bar_times):
    if i == 0:
        notes = [38, 39, 43, 45]
    elif i == 1:
        notes = [42, 43, 38, 39]
    else:
        notes = [43, 45, 43, 38]
    for j, note in enumerate(notes):
        start = time + j * 0.375
        end = start + 0.375
        bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
        bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
# Bar 3: Bbm7 (Bb, D, F, Ab)
# Bar 4: G7 (G, B, D, F)
for i, time in enumerate(bar_times):
    if i == 0:
        # D7: D, F#, A, C#
        notes = [38, 43, 45, 47]
    elif i == 1:
        # Bbm7: Bb, D, F, Ab
        notes = [42, 38, 40, 41]
    else:
        # G7: G, B, D, F
        notes = [43, 45, 38, 40]
    # Comp on 2 and 4
    for j in [1, 3]:
        start = time + j * 0.375
        end = start + 0.375
        for note in notes:
            piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
            piano.notes.append(piano_note)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (38) -> F# (43) -> A (45) -> D (38)
# Play first two notes on bar 2, last two on bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=43, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
