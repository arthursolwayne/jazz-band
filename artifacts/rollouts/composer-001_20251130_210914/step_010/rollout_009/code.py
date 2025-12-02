
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
bar_length = 1.5
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeating notes
# Fm: F, Ab, Bb, D, Eb, G, etc.
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0), # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, D
# Bb7: Bb, Db, Eb, F
# Eb7: Eb, G, Bb, D
# Ab7: Ab, B, Db, E
chords = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # Db
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    # Bar 4: Eb7
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    # Bar 4: Ab7
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125), # E
]
piano.notes.extend(chords)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Start on F (64), play a motif: F (64), G (65), Ab (63), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * bar_length
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
