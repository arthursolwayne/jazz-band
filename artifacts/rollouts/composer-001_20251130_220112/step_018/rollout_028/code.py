
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
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=51, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # D

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5),  # D

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
# Bar 2: Dm7 at beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # F

    # Bar 3: Dm7 at beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # F

    # Bar 4: Dm7 at beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # F
]
piano.notes.extend(piano_notes)

# Drums: same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Sax: Dante - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - G - D (saxophone in Bb, so D is played on C)
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # C (D in Dm)
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25), # D (F in Dm)
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625), # E (G in Dm)
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # C (D in Dm)

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),  # C

    # Bar 4: Finish it
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
