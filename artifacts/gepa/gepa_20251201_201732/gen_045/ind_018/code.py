
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
bar_length = 1.5  # seconds

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane on piano: Cm7 (C, E, G, Bb) -> F7 (F, A, C, E) -> Gm7 (G, Bb, D, F) -> Cm7 (C, E, G, Bb)
# Comp on 2 and 4
bar_start = 1.5
for i in range(2, 5):
    time = bar_start + (i - 2) * 0.375
    if i % 2 == 0:
        # comp on 2 and 4
        if i == 2:
            # Cm7: C, E, G, Bb
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.125))
        elif i == 4:
            # Cm7 again
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.125))
    # Marcus on bass: walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
    if i == 2:
        # Dm root (D2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125))
    elif i == 3:
        # Chromatic approach to G (F#2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=time, end=time + 0.125))
    elif i == 4:
        # G (G2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D - Eb - F - G (ascending), then leave it hanging on G at the end of bar 2, then return in bar 4 with D - Eb - F - G again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=63, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 1.125, end=bar_start + 1.5),
]
sax.notes.extend(sax_notes)

# Repeat the motif in bar 4
bar_start_4 = 3.0
sax_notes_4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start_4, end=bar_start_4 + 0.375),
    pretty_midi.Note(velocity=100, pitch=63, start=bar_start_4 + 0.375, end=bar_start_4 + 0.75),
    pretty_midi.Note(velocity=100, pitch=65, start=bar_start_4 + 0.75, end=bar_start_4 + 1.125),
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start_4 + 1.125, end=bar_start_4 + 1.5),
]
sax.notes.extend(sax_notes_4)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane on piano: F7 (F, A, C, E)
# Comp on 2 and 4
for i in range(2, 5):
    time = bar_start_4 + (i - 2) * 0.375
    if i % 2 == 0:
        # comp on 2 and 4
        if i == 2:
            # F7: F, A, C, E
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=time, end=time + 0.125))
    # Marcus on bass: walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
    if i == 2:
        # Dm root (D2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125))
    elif i == 3:
        # Chromatic approach to G (F#2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=time, end=time + 0.125))
    elif i == 4:
        # G (G2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane on piano: Gm7 (G, Bb, D, F)
# Comp on 2 and 4
for i in range(2, 5):
    time = bar_start_4 + 1.5 + (i - 2) * 0.375
    if i % 2 == 0:
        # comp on 2 and 4
        if i == 2:
            # Gm7: G, Bb, D, F
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=time, end=time + 0.125))
            piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=time, end=time + 0.125))
    # Marcus on bass: walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
    if i == 2:
        # Dm root (D2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.125))
    elif i == 3:
        # Chromatic approach to G (F#2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=39, start=time, end=time + 0.125))
    elif i == 4:
        # G (G2)
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=43, start=time, end=time + 0.125))

# Drums for bars 2-4
for i in range(2, 5):
    time = bar_start + (i - 2) * 0.375
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
