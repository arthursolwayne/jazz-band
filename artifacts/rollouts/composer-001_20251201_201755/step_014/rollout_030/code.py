
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # A2 (root)
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),  # B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # G2 (root)
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625), # B2 (fifth)
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # Bb2 (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F4 (F)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A4 (A)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # C5 (C)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # Eb4 (Eb)
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=3.0),  # Bb4 (Bb)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # D5 (D)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # F5 (F)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # Ab4 (Ab)
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: C7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4 (C)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # E4 (E)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4 (G)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # B4 (B)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - Bb4 - F4 - Eb4 (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=3.0),  # F4 (half note)
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.375), # Bb4 (eighth note)
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75), # F4 (eighth note)
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125), # Eb4 (eighth note)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start, duration):
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start + 2.625, end=start + 3.0)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start + 3.0, end=start + 3.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 3.0, end=start + 3.375)
    snare3 = pretty_midi.Note(velocity=100, pitch=38, start=start + 3.375, end=start + 3.75)
    hihat9 = pretty_midi.Note(velocity=100, pitch=42, start=start + 3.375, end=start + 3.75)
    hihat10 = pretty_midi.Note(velocity=100, pitch=42, start=start + 3.75, end=start + 4.125)
    hihat11 = pretty_midi.Note(velocity=100, pitch=42, start=start + 4.125, end=start + 4.5)
    hihat12 = pretty_midi.Note(velocity=100, pitch=42, start=start + 4.5, end=start + 4.875)
    kick4 = pretty_midi.Note(velocity=100, pitch=36, start=start + 4.5, end=start + 4.875)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 4.875, end=start + 5.25)
    hihat13 = pretty_midi.Note(velocity=100, pitch=42, start=start + 4.875, end=start + 5.25)
    hihat14 = pretty_midi.Note(velocity=100, pitch=42, start=start + 5.25, end=start + 5.625)
    hihat15 = pretty_midi.Note(velocity=100, pitch=42, start=start + 5.625, end=start + 6.0)
    for note in [kick, snare, hihat1, hihat2, hihat3, hihat4, kick2, snare2, hihat5, hihat6, hihat7, hihat8, kick3, snare3, hihat9, hihat10, hihat11, hihat12, kick4, snare4, hihat13, hihat14, hihat15]:
        drums.notes.append(note)

add_drums(1.5, 4.5)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
