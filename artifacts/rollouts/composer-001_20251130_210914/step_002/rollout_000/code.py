
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
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hats on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus's bass line - walking line in Dm, chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # Dm7: D F A C
    # Walking bass line
    if bar == 2:
        # D -> F -> Ab -> C -> D (chromatic approach to Ab)
        notes = [pretty_midi.Note(velocity=90, pitch=62, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=90, pitch=65, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=90, pitch=63, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=90, pitch=67, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        # C -> D -> F -> Ab -> C
        notes = [pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=90, pitch=62, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=90, pitch=65, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=90, pitch=63, start=start + 1.125, end=start + 1.5)]
    elif bar == 4:
        # Ab -> C -> D -> F -> Ab
        notes = [pretty_midi.Note(velocity=90, pitch=63, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=90, pitch=62, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=90, pitch=65, start=start + 1.125, end=start + 1.5)]
    bass.notes.extend(notes)

# Diane's piano - 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # Dm7: D F A C
    if bar == 2:
        # Comp on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=65, start=start + 1.125, end=start + 1.5)
        piano.notes.append(note)
    elif bar == 3:
        # Comp on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=65, start=start + 1.125, end=start + 1.5)
        piano.notes.append(note)
    elif bar == 4:
        # Comp on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=65, start=start + 1.125, end=start + 1.5)
        piano.notes.append(note)

# Little Ray's drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hats on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Dante's saxophone - one short motif, make it sing
# Bar 2: Start the motif
bar2_start = 1.5
sax_note = pretty_midi.Note(velocity=110, pitch=67, start=bar2_start, end=bar2_start + 0.375)
sax.notes.append(sax_note)
# Bar 3: Continue the motif
bar3_start = 3.0
sax_note = pretty_midi.Note(velocity=110, pitch=65, start=bar3_start, end=bar3_start + 0.375)
sax.notes.append(sax_note)
bar3_start += 0.75
sax_note = pretty_midi.Note(velocity=110, pitch=62, start=bar3_start, end=bar3_start + 0.375)
sax.notes.append(sax_note)
# Bar 4: Finish the motif
bar4_start = 4.5
sax_note = pretty_midi.Note(velocity=110, pitch=67, start=bar4_start, end=bar4_start + 0.375)
sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
