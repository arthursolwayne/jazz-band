
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
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),  # Ab
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # B
    # Bar 3: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # B
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # B
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish it
# Motif: F - Ab - Bb - F (1.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=1.625, end=1.75), # C#
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),  # Bb
    # Repeat motif shifted up a half-step
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.125),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=3.125, end=3.25), # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=54, start=3.375, end=3.5),  # B
    # Finish the motif
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=56, start=4.625, end=4.75), # C#
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.125),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.125, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.5),   # Bb
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
