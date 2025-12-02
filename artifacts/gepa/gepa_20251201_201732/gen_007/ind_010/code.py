
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Bar 2: chromatic approach to G2 (up)
    pretty_midi.Note(velocity=70, pitch=39, start=1.875, end=2.125),
    # Bar 2: G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),
    # Bar 3: G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.875),
    # Bar 3: chromatic approach to D2 (down)
    pretty_midi.Note(velocity=70, pitch=42, start=2.875, end=3.125),
    # Bar 3: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=3.125, end=3.5),
    # Bar 4: D2 (root)
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.875),
    # Bar 4: chromatic approach to G2 (up)
    pretty_midi.Note(velocity=70, pitch=39, start=3.875, end=4.125),
    # Bar 4: G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)  # D
note2 = pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0)  # F#
note3 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)  # A
note4 = pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=2.0)  # C#
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: G7 (G-B-D-F)
note1 = pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0)  # G
note2 = pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=3.0)  # B
note3 = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0)  # D
note4 = pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0)  # F
piano.notes.extend([note1, note2, note3, note4])

# Bar 4: D7 (D-F#-A-C)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0)  # D
note2 = pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=4.0)  # F#
note3 = pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0)  # A
note4 = pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=4.0)  # C
piano.notes.extend([note1, note2, note3, note4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F# (67) -> A (71), then repeat but end on A
# Bar 2: D -> F# -> A
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25)
sax.notes.extend([note1, note2, note3])

# Bar 3: D -> F# -> A
note1 = pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0)
note3 = pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25)
sax.notes.extend([note1, note2, note3])

# Bar 4: D -> F# -> A (now end on A)
note1 = pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)
note3 = pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25)
sax.notes.extend([note1, note2, note3])

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_russo_intro.mid')
