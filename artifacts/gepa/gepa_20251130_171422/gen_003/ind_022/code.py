
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
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = [pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125) for i in range(4)]
    drums.notes.extend([kick, snare] + hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
# Fm7 -> Bb7 -> Eb7 -> Ab7
# Fm = F, Ab, C, Db

# Bass line: F, Gb, G, Ab, Bb, B, C, Db (chromatic approach to Bb7)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0), # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5), # Db
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0), # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Db
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
# Ab7 = Ab, C, Eb, Gb

# Bar 2: Fm7 (2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # Db

    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.999), # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.999), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.999), # C
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.999), # Db
]

# Bar 3: Bb7 (2 and 4)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # Ab

    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875), # Ab
])

# Bar 4: Eb7 (2 and 4)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625), # Db

    pretty_midi.Note(velocity=100, pitch=59, start=6.0, end=6.375), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.375), # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=6.0, end=6.375), # Db
])

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, G, Ab, Bb, B, C, Db
# Motif: F -> Gb -> Ab -> C (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=3.0), # F (half note)
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.375), # Gb (quarter)
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75), # Ab (eighth)
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # C (eighth)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = [pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125) for i in range(4)]
    drums.notes.extend([kick, snare] + hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
