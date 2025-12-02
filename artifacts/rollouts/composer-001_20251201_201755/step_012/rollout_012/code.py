
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm (F2 - C2 - Ab2 - Eb2 - Bb2 - F2 - Ab2 - Eb2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # C2
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # Eb2
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # Eb2
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # C2
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375), # D
])
piano.notes.extend(piano_notes)

# Sax: your moment
# One short motif: F, Ab, Bb, C (Fm7 arpeggio with a twist)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=57, start=1.875, end=2.0), # Bb (left hanging)
    # Come back later to finish it
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.9375), # C
]
sax.notes.extend(sax_notes)

# Bar 3: continue the motif with resolution
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.3125, end=4.5), # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875), # C
])

# Bar 4: leave it hanging with a Bb
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=57, start=4.875, end=5.0), # Bb
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
