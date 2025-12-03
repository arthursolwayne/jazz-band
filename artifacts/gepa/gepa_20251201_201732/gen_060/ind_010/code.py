
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm (F, Ab, D, C), roots and fifths with chromatic approaches
# Bar 2: Fm (F, C, Ab, D)
# Bar 3: Bb7 (Bb, F, D, Ab)
# Bar 4: Eb7 (Eb, Bb, G, D)
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm: F, C, Ab, D
        notes = [pretty_midi.Note(velocity=90, pitch=71, start=start, end=start + 0.375),  # F
                 pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75),  # C
                 pretty_midi.Note(velocity=90, pitch=64, start=start + 0.75, end=start + 1.125),  # Ab
                 pretty_midi.Note(velocity=90, pitch=69, start=start + 1.125, end=start + 1.5)]  # D
    elif bar == 3:
        # Bb7: Bb, F, D, Ab
        notes = [pretty_midi.Note(velocity=90, pitch=70, start=start, end=start + 0.375),  # Bb
                 pretty_midi.Note(velocity=90, pitch=71, start=start + 0.375, end=start + 0.75),  # F
                 pretty_midi.Note(velocity=90, pitch=69, start=start + 0.75, end=start + 1.125),  # D
                 pretty_midi.Note(velocity=90, pitch=64, start=start + 1.125, end=start + 1.5)]  # Ab
    elif bar == 4:
        # Eb7: Eb, Bb, G, D
        notes = [pretty_midi.Note(velocity=90, pitch=65, start=start, end=start + 0.375),  # Eb
                 pretty_midi.Note(velocity=90, pitch=70, start=start + 0.375, end=start + 0.75),  # Bb
                 pretty_midi.Note(velocity=90, pitch=71, start=start + 0.75, end=start + 1.125),  # G
                 pretty_midi.Note(velocity=90, pitch=69, start=start + 1.125, end=start + 1.5)]  # D
    bass.notes.extend(notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Fm7
        notes = [pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.75),  # F
                 pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75),  # Ab
                 pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.75),  # C
                 pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)]  # D
    elif bar == 3:
        # Bb7
        notes = [pretty_midi.Note(velocity=100, pitch=70, start=start, end=start + 0.75),  # Bb
                 pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75),  # D
                 pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.75),  # F
                 pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.75)]  # Ab
    elif bar == 4:
        # Eb7
        notes = [pretty_midi.Note(velocity=100, pitch=65, start=start, end=start + 0.75),  # Eb
                 pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.75),  # G
                 pretty_midi.Note(velocity=100, pitch=70, start=start, end=start + 0.75),  # Bb
                 pretty_midi.Note(velocity=100, pitch=69, start=start, end=start + 0.75)]  # D
    piano.notes.extend(notes)

# Sax: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, D, F
# Start on bar 2, leave it hanging on bar 3, resolve on bar 4

# Bar 2
note = pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 0.375, end=1.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)

# Bar 3 (hanging)
note = pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.0 + 0.375)
sax.notes.append(note)

# Bar 4 (resolve)
note = pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.5 + 0.375)
sax.notes.append(note)

# Drums in bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
