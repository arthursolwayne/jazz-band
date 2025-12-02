
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

# Bass: Marcus - walking line, chromatic approaches
# Fm: F, Ab, Bb, Db
# Walking line in Fm: F, Gb, Ab, A, Bb, B, Db, D

bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0), # A
]

bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, C
# Fm7 on 2 and 4

piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # Ab (octave up)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C
]

piano.notes.extend(piano_notes)

# Sax: Dante - short motif, make it sing
# Start with F, then Bb (chromatic), then Ab, then rest
# F (64), Bb (69), Ab (67), rest

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.0625, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875), # F (come back)
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=3.5625, end=3.75), # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.6875), # F (come back again)
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.0625, end=5.25), # F
]

sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth

for bar in range(2, 4):
    start = bar * 1.5
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
midi.write("dante_russo_intro.mid")
